import sys
data = []
for i in range(2):
    data.append(list(map(int,sys.stdin.readline().split())))
N = data[1][0]
X, Y = data[0][0], data[0][1] # X 는 가로길이, Y는 세로길이
y_cut = [] # 가로로 자르는 점선번호들
x_cut = [] # 세로로 자르는 점선번호들
for _ in range(2,N+2):
    a,b = map(int, sys.stdin.readline().split())
    if a == 0:
        y_cut.append(b)
    else:
        x_cut.append(b)
y_cut = [0] + y_cut + [Y]
x_cut = [0] + x_cut + [X]
y_cut = sorted(y_cut) # 오름차순 정렬, len() 만큼 자른다
x_cut = sorted(x_cut)
ny_cut = [None]*(len(y_cut)-1)
nx_cut = [None]*(len(x_cut)-1)
for i in range(len(y_cut)-1):
    ny_cut[i]= y_cut[i+1] - y_cut[i]
for i in range(len(x_cut)-1):
    nx_cut[i]= x_cut[i+1] - x_cut[i]
print(max(nx_cut)*max(ny_cut))



