num = list(
    # 리스트 컴프리헨션: for문에서 생성된 값을 i에 대입 [1, 2, ..., 30]
    i for i in range(1, 31)
)  

for i in range(28):
    num.remove(int(input()))

print(min(num))
print(max(num))
