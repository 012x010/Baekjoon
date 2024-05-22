# 바구니 개수 n, 순으로 바꿀 횟수 m
n, m = map(int, input().split())

# n개의 바구니에 각각 바구니 번호가 붙음
bag = []
for i in range(1, n + 1):
    bag.append(i)

# i번째 바구니부터 j번째 바구니까지 역순 정렬
for _ in range(m):
    i, j = map(int, input().split())
    bag[i - 1 : j] = bag[i - 1 : j][::-1]
    # bag[i:j] -> bag의 i부터 j 앞까지 슬라이싱
    # [::-1] -> 리스트 역순 정렬

# 리스트의 원소를 공백을 포함한 문자열로 합쳐서 출력
output = " ".join(map(str, bag))
print(output)