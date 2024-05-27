n = int(input())

i = 0
floor = 1

while 1:
    i += 1
    if floor >= n:
        break
    floor += 6 * i
    
print(i)