import sys

def sepasa(h):#Tome que se pasa, por lo tanto voy a tomar el 0 mas grande
    agua = 0
    for col in a:
         if h > col:
             agua += h - col
    return agua > x #Return un booleano, siempre (aca esta la logica)

data = iter(sys.stdin.read().split())
t = int(next(data))
for _ in range(t):
    n, x = int(next(data)), int(next(data))
    a = [int(next(data)) for _ in range(n)]

    low, b = 0, max(a) + x + 1 #Busca un numero que si o si sea mas grande que el resultado, para asegurar que el resultado este entre low y b
    while b - low > 1:
            c = (low + b) // 2
            if sepasa(c):
                b = c
            else:
                low = c
        
    print(low)            

 #Uso low en vez de a, por que ya uso a para la lista de las columnas