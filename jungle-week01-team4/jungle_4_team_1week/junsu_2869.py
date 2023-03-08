import sys, math
A,B,V = list(map(int, sys.stdin.readline().split()))
day = (V-A)/(A-B)
print(math.ceil(day)+1)

# numbers = [A, B, V, t] 시간초과 방법1
# while True:
#     numbers[3] += 1
#     if numbers[2]-((numbers[0]-numbers[1])*numbers[3])<=numbers[0]:
#         print(numbers[3])
#         break

# d = 0   시간초과 방법 2
# while True:
#     t += 1
#     d += A
#     if d >= V:
#         break
#     d -= B
# print(t)