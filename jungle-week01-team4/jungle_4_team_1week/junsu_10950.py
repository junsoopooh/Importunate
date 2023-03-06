import sys
T = int(sys.stdin.readline())
for i in range(1,T+1):
    low_list = list(map(int,sys.stdin.readline().split()))
    print(int(low_list[0])+int(low_list[1]))
    low_list.clear()
