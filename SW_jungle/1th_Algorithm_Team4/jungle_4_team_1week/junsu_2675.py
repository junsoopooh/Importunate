import sys
answer = []
T = int(sys.stdin.readline())
for i in range(1, T+1):
    i_test_list = list(sys.stdin.readline().split())
    answer = list(i_test_list[1])
    N = int(i_test_list[0])
    real_answer = [x * N for x in answer]
    print(*real_answer[:] ,sep = '', end="\n")
