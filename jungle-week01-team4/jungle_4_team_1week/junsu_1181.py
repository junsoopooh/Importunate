import sys
N = int(sys.stdin.readline())
data = [sys.stdin.readline().strip() for _ in range(N)]
set_data = set(data)
data = list(set_data)
data.sort()
data.sort(key=len)
for x in data:
    print(x)
