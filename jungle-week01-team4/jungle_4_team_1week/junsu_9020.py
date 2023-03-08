import sys
N = int(sys.stdin.readline())
data = [sys.stdin.readline().strip() for i in range(N)]

def prime(n):
    if n == 1:
        return False
    for i in range(2,int(n**0.5)+1):
            if n % i == 0:
                return False
    return True
for i in range(0,N):
    num = int(data[i])
    a, b = num//2, num//2
    while a > 0:
        if prime(a) and prime(b):
            print(a, b)
            break
        else:
            a -= 1
            b += 1