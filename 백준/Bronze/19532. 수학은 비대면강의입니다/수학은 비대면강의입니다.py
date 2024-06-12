a, b, c, d, e, f = map(int, input().split())

print(int((c*e-b*f) / (e*a-b*d)), int((c*d-a*f) / (b*d-a*e)))