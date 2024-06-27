import sys
input = sys.stdin.readline

n = int(input())    # n개의 정수 입력할 것
a = [0] * 10001     # 각 정수는 10000 이하의 수이므로, 0~10000에 해당하는 10001개의 리스트 생성

for _ in range(n):          # n개의 정수 입력 받아,
    a[int(input())] += 1    # 해당 리스트 값 +1하여, 그 정수가 몇 번 입력되었는지 카운트

for i in range(len(a)):     # 리스트를 돌면서,
    if a[i] != 0:           # 해당 리스트 원소가 0이 아니라면, 1회 이상 등장한 정수라는 뜻이므로
        for _ in range(a[i]):   # 해당 정수가 등장한 횟수(리스트에 저장된 정수)만큼
            print(i)            # 해당 정수 출력