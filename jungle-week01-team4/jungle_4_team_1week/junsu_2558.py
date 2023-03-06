import sys

a = int(sys.stdin.readline())
b = int(sys.stdin.readline())
b_divide = [int(x) for x in str(b)]
print(a*b_divide[2])
print(a*b_divide[1])
print(a*b_divide[0])
print(a*b)