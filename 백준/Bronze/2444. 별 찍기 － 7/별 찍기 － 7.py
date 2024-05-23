n = int(input())

for i in range(n):
    line = ""
    for j in range(n - i - 1):
        line += " "
    for j in range(2 * i + 1):
        line += "*"
    print(line)

for i in range(n - 1):
    line = ""
    for j in range(i + 1):
        line += " "
    for j in range(2 * n - 2 * i - 3):
        line += "*"
    print(line)
