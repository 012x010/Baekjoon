n = int(input())
m = 0

for _ in range(n):
    m += 1
    print(" " * (n - m) + "*" * m)