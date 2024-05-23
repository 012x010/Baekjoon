n = m = int(input())

for _ in range(n):
    print("*" * (n - (m := m - 1)))