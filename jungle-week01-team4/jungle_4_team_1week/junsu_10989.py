import sys
N = int(sys.stdin.readline())
data = [0]*10001
for _ in range(N):
        data[int(sys.stdin.readline())] += 1
for i in range(10001):
    if data[i] != 0:
        for x in range(data[i]):
            print(i)