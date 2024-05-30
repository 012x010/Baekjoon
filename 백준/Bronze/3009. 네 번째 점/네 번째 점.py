a = list(map(int, open(0).read().split()))

x = sorted([a[0], a[2], a[4]])
y = sorted([a[1], a[3], a[5]])

if x[0] != x[1]:
    print(x[0], end=" ")
else:
    print(x[2], end=" ")

if y[0] != y[1]:
    print(y[0])
else:
    print(y[2])
