import sys

from string import ascii_lowercase, ascii_uppercase

x = sys.stdin.readline().strip()
ascci_list = [None] * 123
upper_list = list(ascii_uppercase)
lower_list = list(ascii_lowercase)
for i in range(0,26):
    ascci_list[i+65] = upper_list[i]
for i in range(0,26):
    ascci_list[i+97] = lower_list[i]
for i in range(0,10):
    ascci_list[i+48] = str(i)
def trans(y):
    result = ascci_list.index(y)
    print(result)
trans(x)
