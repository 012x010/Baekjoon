n = int(input())

sum = 1
index = 0

while 1:
    index += sum
    sum += 1
    if index >= n:
        break

if sum % 2 == 0:
    print("%d/%d"%(1 + index - n, sum - index + n - 1))
else:
    print("%d/%d"%(sum - index + n - 1, 1 + index - n))
