n = 15
a = []
for p in range(1, n+1):
    for v in range(1, n+1):
        if n % (p + v) == 0 and p > v:
            a.append(v)
            a.append(p)
print(*a, sep='')

# решение для "12" - # 15 - 12 14 114 23 213 312 411 510 69 78
#                           12 23 14 78 69 510 411 312 213 114
