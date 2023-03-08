import sys

a=int(sys.stdin.readline())

def calculate(a):
    if a%4 == 0:
        calculate2(a)
    else :
        print('0')
def calculate2(a):
    if a%100 == 0:
        calculate3(a)
    else:
        print('1')
def calculate3(a):
    if a%400 == 0:
        print("1")
    else:
        print("0")

calculate(a)
