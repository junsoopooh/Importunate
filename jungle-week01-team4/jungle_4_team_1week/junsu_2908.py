import sys
A, B = map(int, sys.stdin.readline().rstrip().split(' '))

def change(x):
    inner = list(str(x))
    r_inner = inner[::-1]
    return r_inner[0]+r_inner[1]+r_inner[2]
new_A = int(change(A))
new_B = int(change(B))
def choose(M,N):
    if new_A >= new_B:
        print(new_A)
    else:
        print(new_B)
choose(A,B)

# print(max(sys.stdin.readline()[::-1].split()))

