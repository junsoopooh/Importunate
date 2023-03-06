import sys
data = []
for i in range(2):
       data.append(list(map(int, sys.stdin.readline().split())))
def search(a,b):
       if int(a)<int(b):
             print(int(a), end=" ")
       else:
              return

for t in range(data[0][0]):
       search(data[1][t],data[0][1])

