n, *a = map(int, open(0).read().split())
a = sorted(a)
print("\n".join(map(str, a)))