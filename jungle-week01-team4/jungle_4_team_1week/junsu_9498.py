import sys
a = int(sys.stdin.readline())
def grade(a):
    if a >= 90:
        print('A')
    elif 90>a>=80:
        print('B')
    elif 80>a>=70:
        print('C')
    elif 70>a>=60:
        print('D')
    else:
        print('F')
grade(a)
