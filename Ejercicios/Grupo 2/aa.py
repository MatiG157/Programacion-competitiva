n, k = map(int, input().split())

""" def pred(i,rest):
    return (i*5 < rest) """

tiemp = 240 - k
ej = 0

for i in range(1, n+1):
    if i*5 <= tiemp:
        tiemp -= i*5
        ej += 1
    else:
        break

print(ej)