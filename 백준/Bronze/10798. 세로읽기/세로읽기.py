array = []

for _ in range(5):
    row_input = input()
    row = list(str(row) for row in row_input)
    array.append(row)

for i in range(15):
    for j in range(5):
        try:
            print(array[j][i], end="")
        except IndexError:
            continue

print()
