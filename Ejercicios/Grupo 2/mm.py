import sys

data = iter(sys.stdin.read().split())

cases = int(next(data))

for i in range (cases):
    columns = int(next(data))
    water = int(next(data))

    col = []

    for _ in range (columns):
        sig = int(next(data))
        col.append(sig)
    
    lo, hi = 0, max(col) + water
    while hi - lo > 1:
        tot_col = 0
        c = (lo + hi) // 2

        for s in col:
            if s > c:
                s = c
            tot_col += s

        if (columns * c - tot_col) > water:
            hi = c
        else:
            lo = c
    
    print(hi)

# 0 0 0 0 1 1 1 1