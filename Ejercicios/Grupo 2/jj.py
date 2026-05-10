import sys

data = iter(sys.stdin.read().split())

cases = int(next(data))

for i in range (cases):
    health1 = int(next(data))
    health2 = int(next(data))
    health3 = int(next(data))

    total = health1 + health2 + health3
    if total % 9 == 0:
        rounds = total / 9
        if (health1 >= rounds) and (health2 >= rounds) and (health3 >= rounds):
            print('YES')
        else:
            print('NO')
    else:
        print('NO')