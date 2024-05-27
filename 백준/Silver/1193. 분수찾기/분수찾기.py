n = int(input())

sum = 1
index = 0

while 1:
    index += sum
    sum += 1
    if index >= n:
        break

if sum % 2 == 0:
    print(1 + index - n, end="")
    print("/", end="")
    print(sum - index + n - 1)
else:
    print(sum - index + n - 1, end="")
    print("/", end="")
    print(1 + index - n)
