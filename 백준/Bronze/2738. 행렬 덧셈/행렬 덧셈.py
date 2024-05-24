n, m = map(int, input().split())

A = [[0 for j in range(m)] for i in range(n)]

for i in range(n):
    num = list(map(int, input().split()))
    for j in range(m):
        A[i][j] = num[j]

B = [[0 for j in range(m)] for i in range(n)]

for i in range(n):
    num = list(map(int, input().split()))
    for j in range(m):
        B[i][j] = num[j]

C = [[0 for j in range(m)] for i in range(n)]

for i in range(n):
    string = ""
    for j in range(m):
        C[i][j] = A[i][j] + B[i][j]
        string += str(C[i][j]) + " "
    print(string)
