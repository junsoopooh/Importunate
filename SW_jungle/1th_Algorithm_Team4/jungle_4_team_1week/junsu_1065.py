import sys
N = int(sys.stdin.readline())
answer = 0
for i in range(1, N+1):
    num_list = list(map(int, str(i)))
    if i <100:
        answer += 1
    elif num_list[2]-num_list[1] == num_list[1]-num_list[0]:
        answer += 1
print(answer)