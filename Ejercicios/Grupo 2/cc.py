cases = int(input())

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
