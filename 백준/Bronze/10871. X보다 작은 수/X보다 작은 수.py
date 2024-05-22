n, target = map(int, input().split())
num = list(map(int, input().split()))
answer = ""

for i in range(n):
    if num[i] < target:
        answer += str(num[i]) + " "

print(answer)
