N, B = input().split()  # N, B 입력
N = N[::-1]  # N을 거꾸로 뒤집음
B = int(B)

result = 0

for i in range(len(N)):
    try:
        result += int(N[i]) * (B**i)
    except ValueError:
        result += (ord(N[i].upper()) - 55) * (B**i)

print(result)
