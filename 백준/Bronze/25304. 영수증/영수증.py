total = int(input())
n = int(input())

for i in range(n) :
    price, n = map(int, input().split())
    total -= price*n

if(total==0):
    print("Yes")
else:
    print("No")