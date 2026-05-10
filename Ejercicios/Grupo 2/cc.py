""" cases = int(input())

for i in range (cases):
    cant, div = map(int, input().split())

    if cant == 1:
        print(div)
    elif div == cant or cant % div == 0:
        print(1)
    elif div < cant:
        if cant % div == 0:
            print(1)
        else:
            print(2)
    elif div % cant == 0:
        print(2)
    else:
        n = (div // cant) + 1
        print(n)
 """

import sys

data = iter(sys.stdin.read().split())

cases = (next(data))

def sirve(k, num, leng):
    minim = (k-1) * leng
    for _ in range (k):
        if minim % num == 0:
            return True
        minim += 1
    return False


for i in range (cases):
    leng = (next(data))
    target = (next(data))

    lo, hi = 0, target
    while hi - lo > 1:
        c = (lo + hi) // 2
        if alcanza(c, target, leng):
            hi = c
        else:
            lo = c

    print(hi) 