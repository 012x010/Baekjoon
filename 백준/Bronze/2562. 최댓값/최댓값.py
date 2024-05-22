num = []

for i in range(9):
    num.append(int(input()))

target = max(num)

print(target)
print(num.index(target) + 1)
