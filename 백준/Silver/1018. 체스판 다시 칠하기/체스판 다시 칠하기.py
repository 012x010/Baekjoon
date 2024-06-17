# 행, 열 크기 입력
n, m = map(int, input().split())
output = []

# 2차원 배열로 저장
origin = [[0 for _ in range(m)] for _ in range(n)]

for i in range(n):
    line = input()

    for j in range(m):
        origin[i][j] = line[j]


for i in range(n - 7):  # 선택영역 시작행
    for j in range(m - 7):  # 선택영역 시작열
        for r in range(2):
            if r == 0:
                count = 0
            else:
                count = 1
            string = [row[:] for row in origin]  # origin의 복사본을 string에 저장

            # 선택영역 첫행 색칠
            for a in range(j + 1, j + 8):
                if string[i][a - 1] == string[i][a]:
                    count += 1
                    string[i][a] = chr(ord("W") + ord("B") - ord(string[i][a]))

            # 선택영역 첫열 색칠
            for b in range(i + 1, i + 8):
                if string[b - 1][j] == string[b][j]:
                    count += 1
                    string[b][j] = chr(ord("W") + ord("B") - ord(string[b][j]))

            for a in range(i + 1, i + 8):
                for b in range(j + 1, j + 8):
                    if (
                        string[a - 1][b] == string[a][b]
                        or string[a][b - 1] == string[a][b]
                    ):
                        count += 1
                        string[a][b] = chr(ord("W") + ord("B") - ord(string[a][b]))

            # string[i][j]를 반대로 전환
            origin[i][j] = chr(ord("W") + ord("B") - ord(origin[i][j]))

            output.append(count)

print(min(output))