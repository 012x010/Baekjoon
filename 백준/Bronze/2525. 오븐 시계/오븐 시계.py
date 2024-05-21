hr, min = map(int, input().split())
timer = int(input())


if(min+timer%60 >= 60) :
    hr = hr+timer//60+1
    min = min+timer%60-60
else :
    hr = hr+timer//60
    min = min+timer%60

if(hr>=24) :
    hr = hr-24

print(hr, min)