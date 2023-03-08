import sys
from itertools import permutations
n = int(sys.stdin.readline())
k = int(sys.stdin.readline())
cards = []
for _ in range(0,n):
    cards.append(sys.stdin.readline().rstrip())
res = set()
for per in permutations(cards, k):
    res.add(''.join(per))

print(len(res))
