n, k, *score = map(int, open(0).read().split())
score = sorted(score)
print(score[n - k])