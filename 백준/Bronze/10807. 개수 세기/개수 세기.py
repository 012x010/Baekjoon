n = int(input())
num = list(map(int, input().split()))
target = int(input())

count = 0

for i in range(n):
    if num[i] == target:
        count += 1

print(count)
