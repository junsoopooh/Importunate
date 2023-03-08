import sys
N = int(sys.stdin.readline())
data = [int(sys.stdin.readline().strip()) for i in range(N)]
data.sort()
for x in data:
    print(x)