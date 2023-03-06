import sys
data = [None] * 3
for i in range(0, 3):
    data[i] = int(sys.stdin.readline())
x = 0
result = data[0]*data[1]*data[2]
new_result = str(result)
new_data = list(new_result)
for i in range(0, 10):
    x = new_data.count(i)
    # print(x)
for i in new_data:
    print(type(i))
    