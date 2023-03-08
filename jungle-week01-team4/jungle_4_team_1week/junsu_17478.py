import sys
N = int(sys.stdin.readline())
blank = '____'
start_sentence = '어느 한 컴퓨터공학과 학생이 유명한 교수님을 찾아가 물었다.'
sentence1 = '"재귀함수가 뭔가요?"' 
sentence2 ='"잘 들어보게. 옛날옛날 한 산 꼭대기에 이세상 모든 지식을 통달한 선인이 있었어.'
sentence3 ='마을 사람들은 모두 그 선인에게 수많은 질문을 했고, 모두 지혜롭게 대답해 주었지.'
sentence4 ='그의 답은 대부분 옳았다고 하네. 그런데 어느 날, 그 선인에게 한 선비가 찾아와서 물었어."'
end_sentence = '라고 답변하였지.'
answer = '"재귀함수는 자기 자신을 호출하는 함수라네"'
def bond(i):
    if i > 0:
        bond(i-1)
        print(blank*(i-1)+sentence1)
        print(blank*(i-1)+sentence2)
        print(blank*(i-1)+sentence3)
        print(blank*(i-1)+sentence4)
        i -= 1
def finish(i):
    if i > 0:
        print(blank*(i-1)+end_sentence)
        finish(i-1)
        i -= 1

print(start_sentence)
bond(N)
print(blank*(N)+sentence1)
print(blank*(N)+answer)
print(blank*(N)+end_sentence)
finish(N)




    
