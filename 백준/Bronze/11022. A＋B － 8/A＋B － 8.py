import sys


case = int(input())

for i in range(case) :
    a, b = map(int,sys.stdin.readline().split())
    print("Case #" + str(i+1) + ":", a, "+", b, "=", a+b)