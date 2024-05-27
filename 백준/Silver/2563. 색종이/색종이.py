n = int(input())

array = [[0] * 100 for _ in range(100)]  # 100*100으로 도화지 초기화

for _ in range(n):
    x, y = map(int, input().split())

    for i in range(x, x + 10):
        for j in range(y, y + 10):
            array[i][j] = 1  # 10*10 사각형 차지하는 부분 1로 표시

area = 0

for k in range(100):
    area += array[k].count(1)  # 행을 돌면서 1개수 count

print(area)
