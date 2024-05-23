credit = 0
score = 0

grade_list = [
    ("A+", 4.5),
    ("A0", 4.0),
    ("B+", 3.5),
    ("B0", 3.0),
    ("C+", 2.5),
    ("C0", 2.0),
    ("D+", 1.5),
    ("D0", 1.0),
    ("F", 0.0),
]


for i in range(20):
    school = list(map(str, input().split()))

    if school[2] == "P" :
        continue

    value = [value for grade, value in grade_list if grade == school[2]]

    credit += float(school[1])
    score += value[0] * float(school[1])

if credit == 0:
    print("{:.6f}".format(0.000000))  # 출력: 0.000000
else:
    print("{:.6f}".format(score / credit))  # 소수점 6자리까지 포맷
