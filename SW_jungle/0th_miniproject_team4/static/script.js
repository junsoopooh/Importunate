$(document).ready(function () {
    const token = $.cookie("mytoken");
    if (token) {
        // 토큰이 있을 경우 즉, 로그인한 경우
        $('#btn-login').hide();
        $('#btn-signup').hide();

        $('#btn-logout').show();
        $('#btn-mypage').show();

    

        // showMBTIresult()
    } else {
        // 토큰이 없을 경우
        $('#btn-login').show();
        $('#btn-signup').show();

        $('#btn-logout').hide();
        $('#btn-mypage').hide();
    }
});

function signin(){
    let id = $('#input-id').val();
    let pw = $('#input-pw').val();

    $.ajax({
        type: "POST", 
        url: "/login", 
        data: {'id_give': id, 'pw_give': pw},
        success: function (response) {
            if (response["result"] == "success") {
                $.cookie("mytoken", response["token"], { path: "/" });
                alert("로그인 성공!");
                // 성공 시 메인페이지로 이동
                window.location.href = "/listpage";
            } else {
                alert("아이디 및 비번을 확인해주세요.")
            }
        }
    })
}

function logout() {
    $.removeCookie('mytoken', { path: '/' });
    // 로그아웃 후, 새로고침
    window.location.href = "/";
}

$(document).ready(function () {
    showHobby();
});

function showHobby() {
    $.ajax({
        type: "GET",
        url: "/mypage/hobbySelected",
        data: {},
        success: function (response) {
            let sports = response.hobby[0].sports;
            let coding = response.hobby[0].coding;
            let etc = response.hobby[0].etc;

            // String to Boolean : $parseJSON('true')
            $("input:checkbox[id='sports']").prop("checked", $.parseJSON(sports));
            $("input:checkbox[id='coding']").prop("checked", $.parseJSON(coding));
            $("input:checkbox[id='etc']").prop("checked", $.parseJSON(etc));
        }
    })
}

function editHobby() {
    let sports_selected = $("#sports").is(":checked");
    let coding_selected = $("#coding").is(":checked");
    let etc_selected = $("#etc").is(":checked");

    if (!$("input:checkbox:checked").length) {
        alert("취미를 선택해주세요!")
        return
    }

    $.ajax({
        type: "PUT",
        url: "/mypage",
        data: {
            'sports_give': sports_selected,
            'coding_give': coding_selected,
            'etc_give': etc_selected,
        },
        success: function (response) {
            if (response["result"] == "success") {
                alert("취미 수정 성공!");
                // 성공 시 새로고침
                window.location.reload();
            } else {
                alert("서버 오류!")
            }
        }
    })
}

function editPassWord() {
    const inputName = prompt('가장 존경하는 선생님 이름은?')

    if (!inputName) {
        alert('존경하는 선생님 이름을 입력해주세요!')
        return
    }

    $.ajax({
        type: "POST",
        url: "/mypage",
        data: { 'teacherName_give': inputName, },
        success: function (response) {
            if (response["result"] == "success") {
                const inputPassWord = prompt('변경할 비밀번호 : ')

                if (!inputPassWord) {
                    alert('변경할 비밀번호를 입력해주세요!')
                    return
                }

                $.ajax({
                    type: "PATCH",
                    url: "/mypage",
                    data: { 'modPassWord_give': inputPassWord, },
                    success: function (response) {
                        if (response["result"] == "success") {
                            alert('비밀번호 변경완료!')
                            // 성공 시 로그인페이지로 이동
                            window.location.href = "/login";
                        } else {
                            alert("회원정보 불일치! 존경하는 선생님 이름을 확인해주세요!")
                        }
                    }
                })

            } else {
                alert("회원정보 불일치! 존경하는 선생님 이름을 확인해주세요!")
            }
        }
    })


}

function postUser(){
    let id = $('#input-id').val();
    let pw = $('#input-pw').val();
    let teacher = $('#input-teacher').val();
    let sports_selected = $("#sports").is(":checked");
    let coding_selected = $("#coding").is(":checked");
    let etc_selected = $("#etc").is(":checked");

    if(id=="" || pw=="" || teacher==""){
        alert("값을 입력해 주세요!");
        return;
    }

    if(!$("input:checkbox:checked").length){
        alert("취미를 선택해주세요!")
        return
    }

    $.ajax({
        type: "POST", 
        url: "/signup", 
        data: {
            'id_give': id, 
            'pw_give': pw, 
            'teacher_give': teacher,
            'sports_give' :sports_selected,
            'coding_give' :coding_selected,
            'etc_give' :etc_selected,
        },
        success: function (response) {
            if (response["result"] == "success") {
                alert("회원가입 성공!");
                // 성공 시 로그인페이지로 이동
                window.location.href = "/login";
            } else {
                alert("서버 오류!")
            }
        }
    })
}


function getCheckboxValue() {
    if ($("input:checkbox:checked").length !== 1) {
        alert("주의!! 모임 목적은 한가지만 선택해야 합니다!!");
        return;
    }

    // 선택된 목록 가져오기
    const query = 'input[name="hobby"]:checked';
    const selectedEls =
        document.querySelectorAll(query);

    // 선택된 목록에서 value 찾기
    let result = '';
    selectedEls.forEach((el) => {
        result += el.value + ' ';
    });

    // 출력
    document.getElementById('result').innerText
        = result;
}

function postgroup() {

    let hobby = document.getElementById('result').innerText;
    let comment = $("#comment").val();
    // let image = document.getElementById("#photo");
    let start = document.querySelector("#start").value;
    let end = document.querySelector("#end").value;
    let maxpeople = $("#maxpeople").val();

    if (new Date(start) >new Date(end)){
        alert("종료날짜는 시작날짜보다 뒤여야 합니다.");
        return;
    }

    // 2. memo에 POST 방식으로 메모 생성 요청하기
    $.ajax({
        type: "POST", // POST 방식으로 요청하겠다.
        url: "/register", // /memo라는 url에 요청하겠다.
        data: {
            hobby_give: hobby,
            comment_give: comment,
            // image_give: image,
            start_give: start,
            end_give: end,
            maxpeople_give: maxpeople,
        }, // 데이터를 주는 방법
        success: function (response) { // 성공하면
            if (response["result"] == "success") {
                alert("등록 성공!");
                // 3. 성공 시 리스트 새로고침하기
                window.location.href = "/listpage";

            } else {
                alert("서버 오류!")
            }
        }
    })
}

$(document).ready(function () {
    showlist();
});
function showlist() {
    $("#cards-box").html("");
    $.ajax({
        type: "GET",
        url: "/listpage_hall",
        data: {},
        success: function (response) {
            let registerList = response['registerList'];
            for (let i = 0; i < registerList.length; i++) {
                makeCard(
                    registerList[i]["hobby"],
                    registerList[i]["comment"],
                    registerList[i]["userid"],
                    registerList[i]["start"],
                    registerList[i]["end"],
                    registerList[i]["nowpeople"],
                    registerList[i]["maxpeople"],
                    registerList[i]["nickname"]
                )
            }
        }
    });
}

function makeCard(hobby, comment, userid, start, end, nowpeople, maxpeople, nickname) {
    let tempHtml = `<tr align="center" bgcolor="white">
        <td>${hobby}</td>
        <td>${comment}</td>
        <td>${userid}</td>
        <td>${start}</td>
        <td>${end}</td>
        <td>${nowpeople}</td>
        <td>${maxpeople}</td>
        <td><button onclick="attend(${nickname})">참가</button></td>
    </tr>`;
    $("#cards-box").append(tempHtml);
}

function attend(nickname) {
    console.log(nickname)
    $.ajax({
        type: "POST",
        url: "/listpage_hall",
        data: { 'num': nickname },
        success: function (response) {
            if (response['result'] == 'success') {
                // 2. '좋아요 완료!' 얼럿을 띄웁니다.
                alert('참가 신청 완료!');
                // 3. 변경된 정보를 반영하기 위해 카드 리스트를 다시 만듭니다.
                showlist();

            }
            else if (response['result'] == 'already') {
                alert('이미 참여한 모임입니다.');
                showlist();
            }
            else if (response['result'] == 'full') {
                alert('인원이 꽉찼습니다!');
                showlist();
            }
            else {
                alert('서버오류!');
            }
        }
    })
}

