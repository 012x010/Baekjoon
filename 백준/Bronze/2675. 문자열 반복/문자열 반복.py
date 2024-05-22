case = int(input())

for _ in range(case):
    n, string = input().split()
    output = ""

    for i in range(len(string)):
        for j in range(int(n)):
            output += string[i]

    print(output)
