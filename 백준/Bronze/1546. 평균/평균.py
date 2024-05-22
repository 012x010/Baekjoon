# 시험 본 과목 개수
n = int(input())


# 시험 점수 리스트 초기화
score = list(map(int, input().split()))

if len(score) != n:
    quit()

# 최고점 기준으로 각 과목 점수 조작
m = max(score)
for i in range(n):
    score[i] = score[i] / m * 100

# 평균 계산
total = 0
for i in range(n):
    total += score[i]

print(total / n)
