# 검은색 체스말과 흰색 체스말 개수 초기화
black = [1, 1, 2, 2, 2, 8]
white = list(map(int, input().split()))

# 개수 차이를 저장할 리스트
piece = []

# 흰색 체스말이 잘못된 개수 저장
for i in range(6):
    piece.append(black[i] - white[i])

# 공백을 포함한 문자열로 출력
output = " ".join(map(str, piece))
print(output)
