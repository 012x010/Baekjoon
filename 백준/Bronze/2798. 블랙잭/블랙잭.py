n, m, *a = map(int, open(0).read().split())
max = 0

for i in range(n-2):
    for j in range(i+1, n-1):
        for k in range(j+1, n):
            total = a[i]+a[j]+a[k]
            if total >= max and total <= m:
                max = total

print(max)