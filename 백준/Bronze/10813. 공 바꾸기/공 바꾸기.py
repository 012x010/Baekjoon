# n은 바구니의 개수, m은 바구니에 공을 바꿀 횟수
n, m = map(int, input().split())

# 바구니 초기화
bag = []

# n개의 바구니에 바구니 번호와 같은 번호의 공이 담겨있음
for _ in range(1, n + 1):
    bag.append(_)

# i번째 바구니와 j번째 바구니의 공을 바꿔 넣기 m회 반복
for _ in range(m):
    i, j = map(int, input().split())
    temp = bag[i - 1]
    bag[i - 1] = bag[j - 1]
    bag[j - 1] = temp

# 리스트의 원소를 공백을 포함한 문자열로 합쳐서 출력
output = " ".join(map(str, bag))
print(output)
