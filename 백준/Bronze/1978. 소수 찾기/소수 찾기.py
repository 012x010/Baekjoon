n, *a = map(int, open(0).read().split())
count = 0

for i in range(n):
    for j in range(2, a[i] + 1):
        if a[i] % j == 0:
            if a[i] == j:
                count += 1
            else:
                break

print(count)