# n은 바구니의 개수, m은 바구니에 공을 넣을 횟수
n, m = map(int, input().split())

# 바구니 초기화
bag = []

# n개의 바구니에 0개의 공이 담겨있음
for _ in range(n):
    bag.append(0)

# i번째 바구니부터 j번째 바구니까지 k라는 공을 넣기 m회 반복
for _ in range(m):
    i, j, k = map(int, input().split())
    for _ in range(i, j + 1):
        bag[_ - 1] = k

# 리스트의 원소를 공백을 포함한 문자열로 합쳐서 출력
output = " ".join(map(str, bag))
print(output)
