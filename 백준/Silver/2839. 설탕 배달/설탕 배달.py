sugar = int(input())
bag = []

for five in range(sugar // 5 + 1):
    for three in range(sugar // 3 + 1):
        if five * 5 + three * 3 == sugar:
            bag.append(five + three)

if len(bag) == 0:
    print(-1)
else:
    print(min(bag))