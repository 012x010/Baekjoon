while 1 :
    a = list(map(int, input().split()))

    if sum(a) == 0:
        break

    a = sorted(a)

    if a[0]+a[1] <= a[2]:
        print("Invalid")
    elif a[0] == a[1] and a[0] == a[2]:
        print("Equilateral")
    elif a[0] == a[1] or a[1] == a[2]:
        print("Isosceles")
    else:
        print("Scalene")