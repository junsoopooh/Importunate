import sys
data = []
for i in range(9):
    data.append(int(sys.stdin.readline()))
print(max(data))
print((data.index(max(data))+1))
