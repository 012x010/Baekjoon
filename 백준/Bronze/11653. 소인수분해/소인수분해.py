n = int(input())

# n == 1이면 아무것도 출력하지 않고

for i in range(2, n + 1):
    if n % i == 0:          # n을 2부터 차례대로 나누는데
        while n % i == 0:   # i로 나누어 떨어지면, 더이상 나누어 떨어지지 않을 때까지 나누기
            print(i)
            n = n / i