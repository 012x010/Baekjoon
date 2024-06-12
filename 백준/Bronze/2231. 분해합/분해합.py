N = input()
n = N

const = ['0']

while int(n) > 0:
    total = 0

    for i in range(len(n)):
        total += int(n[i])

    total += int(n)

    if total == int(N):
        const.append(n)

    n = str(int(n)-1)

print(const[-1])