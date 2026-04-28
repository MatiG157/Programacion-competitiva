n, k = map(int, input().split())

tiempopararesolver = 240 - k

t = 0
c = 0
for i in range(1, n+1):
    t = t + (5*i)
    if t <= tiempopararesolver:
        c = c + 1
    else:
        break
print(c)  
