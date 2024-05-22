# 다이얼 알파벳 치환을 위한 리스트
dial = ["ABC", "DEF", "GHI", "JKL", "MNO", "PQRS", "TUV", "WXYZ"]

# 문자열 입력
string = input()
output = 0

# 문자열 첫번째 문자부터 돌면서
for i in range(len(string)):
    # dial 첫번째 요소부터 돌면서
    for j in dial:
        # 해당 문자가 해당 다이얼에 들어있다면
        if string[i] in j:
            # 소요시간 덧셈
            output += dial.index(j) + 3

print(output)