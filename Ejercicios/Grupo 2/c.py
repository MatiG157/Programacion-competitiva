t = int(input())

for i in range(t):
    n, k = map(int, input().split())

    # 1. Si n > k, necesitamos encontrar el múltiplo de k más cercano
    # para que la suma sea al menos n.
    if n > k:
        # Esto escala k para que sea el primer múltiplo >= n
        k = ((n + k - 1) // k) * k
    
    # 2. Ahora repartimos esa k (que es nuestra suma total) entre n
    # El máximo elemento mínimo es la división redondeada hacia arriba
    resultado = (k + n - 1) // n
    
    print(resultado)