import sys
from itertools import combinations
N, M = map(int,sys.stdin.readline().split())
data = list(map(int, input().split()))
high_score = 0
for i in combinations(data, 3):
    temp_sum = sum(i)
    if high_score < temp_sum <= M:
        high_score = temp_sum
print(high_score)

#     score=[sum(i) for i in range(N*N*N)]
# print(max(score))       