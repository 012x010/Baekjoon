import sys

n = int(input())
p = [[0 for _ in range(2)] for _ in range(n)]

for i in range(n):
    p[i][0], p[i][1] = map(int, sys.stdin.readline().split())

p.sort()

for i in range(n):
    print(p[i][0], p[i][1])
