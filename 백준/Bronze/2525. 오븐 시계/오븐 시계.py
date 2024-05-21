hr, min = map(int, input().split())
timer = int(input())

print((hr+(timer//60)+(min+timer%60)//60)%24, (min+timer%60)%60)