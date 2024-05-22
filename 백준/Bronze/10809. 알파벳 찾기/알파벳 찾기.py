# 문자열 입력 받기
string = input()

# 소문자 비교를 위한 초기화
alpha = "abcdefghijklmnopqrstuvwxyz"
index = []

# index는 기본 -1(해당 알파벳 없음)으로 초기화
for i in range(len(alpha)):
    index.append(-1)

# 알파벳 1개씩, 입력문자열과 비교하여
for i in range(len(alpha)):
    for j in range(len(string)):
        if alpha[i] == string[j]:   # 가장 처음 일치하는 위치의 인덱스를
            index[i] = j            # index 리스트에 저장하고
            break                   # 더이상 그 입력문자열 뒷부분은 보지 않고 break

# 리스트의 원소를 공백을 포함한 문자열로 합쳐서 출력
output = " ".join(map(str, index))
print(output)
