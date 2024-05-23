import re

string = input()
croatia = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]

for c in croatia:
    string = re.sub(c, "0", string)

print(len(string))
