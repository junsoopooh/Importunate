import sys
N = int(sys.stdin.readline())
def result(x):
    answer = 1
    for i in range(1,x+1):
        answer *= i
    print(answer)
result(N)