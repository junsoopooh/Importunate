import sys
N = int(sys.stdin.readline())
pos = [0]*N # 각 열(세로줄)에 배치
flag_a = [False]*N #각 행(가로줄)
flag_b = [False]*(2*N-1) # 
flag_c = [False]*(2*N-1) #
data = []
def plus_answer():
    data.append('answer')
def set(i: int) -> None:
    for j in range(N):
        if(     not flag_a[j]
            and not flag_b[i + j]
            and not flag_c[i - j + N-1]):
            pos[i] = j
            if i == N-1:
                plus_answer()           
            else:
                flag_a[j] = flag_b[i + j] = flag_c[i - j + N-1] = True
                set(i+1)
                flag_a[j] = flag_b[i + j] = flag_c[i - j + N-1] = False 
set(0)
print(len(data))