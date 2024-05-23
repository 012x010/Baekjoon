string = input()

for i in range(round(len(string) / 2 + 0.5)):
    if string[i] == string[len(string) - i - 1]:
        output = 1
    else:
        output = 0
        break

print(output)