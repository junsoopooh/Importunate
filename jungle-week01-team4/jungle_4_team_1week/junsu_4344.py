import sys

C = int(sys.stdin.readline())
group = []
for q in range(1,C+1):
    group = list(map(int, sys.stdin.readline().split()))
    sum = 0
    student = group[0]
    for w in range(1, student+1):
        sum += int(float(group[w]))
    av = sum/student
    filter_group = []
    for i in range(1,student+1):
        if group[i] > av:
            filter_group.append(group[i])
    answer = len(filter_group) / student * 100.0
    print("%0.3f%%"% answer)