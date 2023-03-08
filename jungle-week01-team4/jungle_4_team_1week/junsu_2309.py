import sys
from itertools import combinations
data = [0]*9
for x in range(9):
    data[x]=int(sys.stdin.readline().strip())
for i in combinations(data, 7):
    if sum(i) == 100:
        for j in sorted(i):
            print(j)
        break
