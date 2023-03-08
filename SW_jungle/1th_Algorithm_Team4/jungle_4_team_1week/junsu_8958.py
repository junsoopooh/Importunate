import sys

N = int(sys.stdin.readline())

for i in range(N):
    question=list(sys.stdin.readline())
    total = 0
    plus = 0
    for u in question:
        if (u == 'O'):
            plus += 1
            total += plus
        else:
            plus = 0
    print(total)
