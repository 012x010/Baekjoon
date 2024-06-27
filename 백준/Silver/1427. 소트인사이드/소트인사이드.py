n = input()
a = []

for i in range(len(n)):
    a.append(int(n[i]))

a.sort()
a.reverse()

print("".join(map(str, a)))