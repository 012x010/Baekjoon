hr, min = map(int, input().split())

if(min >= 45) :
    print(hr, min-45)
else :
    if(hr>=1) :
        print(hr-1, min+15)
    else :
        print(23, min+15)