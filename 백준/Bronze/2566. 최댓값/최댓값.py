num = list(map(int, open(0).read().split()))
index = num.index(max(num))
print(max(num))
print(index // 9 + 1, index % 9 + 1)