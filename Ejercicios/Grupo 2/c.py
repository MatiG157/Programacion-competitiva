import sys
datos = iter(sys.stdin.read().split())
t = int(next(datos))
for _ in range(t):
    n, k = int(next(datos)), int(next(datos))
    
objetivo = ((n + k - 1) // k) * k
     
def alcanza(M):
    return n * M >= objetivo

a, b = 0, k   

while b - a > 1:
        c = (a + b) // 2
        if alcanza(c):
            b = c
        else:
            a = c
print(b)            

#Ej 4 lugares 
#3 es el objetivo (la suma sea por ese k)

#  ((4 + 3 - 1) // 3) *     3 = 6 objetivo 
# Div redondeada de 4  3

# 4 / 3 = 1.333

# 1.333 * 3 = 4
# (redondeando para abajo) 1 * 3 = 3 => multiplo de 3 pero menor que 4
# 2 * 3 = 6 El multiplicar por el numero redondeado para arriba, te asegura que el resultado es multiplo de 3 y mayor o igual a 4, lo que es el objetivo.
