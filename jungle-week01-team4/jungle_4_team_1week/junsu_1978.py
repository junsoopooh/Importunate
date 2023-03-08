import sys
N = int(sys.stdin.readline())
data = map(int,sys.stdin.readline().split())
answer = 0
for num in data:
    error = 0
    if num > 1:
        for i in range(2,num):
            if num % i == 0:
                error += 1
        if error == 0:
            answer += 1
print(answer)