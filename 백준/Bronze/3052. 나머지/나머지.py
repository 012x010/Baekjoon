# 정수 입력받을 리스트 초기화
num = []

# 입력받은 10개의 정수로 리스트 생성
for i in range(10):
    num.append(int(input()))

# 나머지 값 저장할 리스트 초기화
div = []

# 42로 나눈 나머지로 리스트 생성
for i in range(10):
    div.append(num[i] % 42)

# div를 정렬해서 저장 sorted
div = sorted(div)

# 서로 다른 나머지가 몇개인지 세기 위한 count 초기화
count = 1

# 정렬한 div의 이웃하는 값을 비교하여, 서로 다르면 count 올리기
for i in range(1, 10):
    if div[i - 1] != div[i]:
        count += 1

print(count)
