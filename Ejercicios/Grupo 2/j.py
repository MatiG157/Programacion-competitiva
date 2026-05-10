import sys

data = iter(sys.stdin.read().split())

cases = int(next(data))

for i in range (cases):
    health1 = int(next(data))
    health2 = int(next(data))
    health3 = int(next(data))
    
    s = (health1 + health2  + health3)
    

    if s % 9 == 0: #Divido por 9 para tener en cuenta el tiro triple (si divido por 18)
        rounds = s / 9
        if  (health1 >= rounds) and (health2 >= rounds) and (health3 >= rounds):
            print("YES")
        else:
            print('NO')
    else: 
        print("NO")

    # 1 8 9 Tiene que la vida minimamente mayor a s/9 sino lo mato antes con el 7mo tiro
