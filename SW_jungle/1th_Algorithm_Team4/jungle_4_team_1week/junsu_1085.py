import sys
x,y,w,h = map(int, sys.stdin.readline().split())

def findx(x) :
    if w/2 > x :
        return x
    else:
        return w-x
def findy(y) :
    if h/2 > y :
        return y
    else:
        return h-y   
xx = findx(x)
yy = findy(y)
def findr(xx,yy) :
    if xx>yy :
        print (yy)
    else:
        print (xx)
findr(xx,yy)

