n = int(input())

string = ""

for i in range(n):
    for j in range(i+1):
        string+="*"
    print(string)
    string = ""