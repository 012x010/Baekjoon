n = int(input())

for _ in range(n):
    exc = int(input())
    print(exc // 25, exc % 25 // 10, exc % 25 % 10 // 5, exc % 25 % 10 % 5)