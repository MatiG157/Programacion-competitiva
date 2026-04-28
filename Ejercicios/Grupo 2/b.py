t = int(input())
for i in range(t):
    n = int(input()) #Se puede omitir esta línea si no se necesita el número de elementos
    num = 0
    a = map(int, input().split()) #Forma de leer una lista de números en una sola línea
    num = sum(a)
    raiz = int(num ** 0.5) #Necesario pasarlo a entero para evitar problemas de precisión con números grandes
    if raiz * raiz == num:
        print('YES')
    else:
        print('NO')
        