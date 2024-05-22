# 두 입력수를 문자열로 저장
num1, num2 = input().split()

# 문자열 역순 재배열 [::-1]
num1 = num1[::-1]
num2 = num2[::-1]

# 두 문자열을 정수로 바꾼 후에 max 출력
num = [int(num1), int(num2)]
print(max(num))