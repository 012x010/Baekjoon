from collections import Counter


# 대소문자 구별하지 않으려면 lower, upper 함수 사용
string = input().upper()

# 알파벳 별 빈도수 딕셔너리 반환 Counter
counter = Counter(string)  # counter : Counter({'Q': 3, 'I': 3, 'W': 1})

# 알파벳 별 빈도수 튜플 반환 most_common(int n) -> 최빈값 n개 출력, int 비우면 모두 출력
common = counter.most_common()  # common : [('Q', 3), ('I', 3), ('W', 1)]

# 최빈값 -> common 튜플의 0번 튜플의 1번 인덱스
max = common[0][1]

# 최빈값과 빈도수count가 같은 문자char을 max_list에 저장
max_list = [char for char, count in common if count == max]  # max_list : ['Q', 'I']

# max_list에 최빈 문자가 여러개라면 ? 출력
if len(max_list) > 1:
    print("?")
else:
    print(max_list[0])
