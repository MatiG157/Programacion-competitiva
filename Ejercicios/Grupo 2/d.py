import sys

# Leemos n (cantidad de puertas)
n = int(sys.stdin.readline())
# Leemos la lista de personas en cada puerta
a = list(map(int, sys.stdin.readline().split()))

tiempos_de_entrada = []

for i in range(n):
    # i es la posición de la puerta (0, 1, 2...)
    # a[i] es cuánta gente hay en esa puerta
    
    # CALCULAMOS EL MOMENTO EXACTO EN QUE ESA PUERTA SE VACÍA:
    # 1. ¿Cuántas vueltas completas tiene que esperar?
    # Usamos (a[i] - i) porque Allen ya "gastó" i minutos en llegar
    vueltas = (max(0, a[i] - i) + n - 1) // n
    
    # 2. El minuto exacto en que entra por esa puerta i
    minuto_entrada = vueltas * n + i
    
    # Guardamos ese minuto
    tiempos_de_entrada.append(minuto_entrada)

# LA RESPUESTA ES: La puerta que tenga el MINUTO DE ENTRADA más chico
# Buscamos la posición del valor mínimo en nuestra lista de tiempos
min_valor = min(tiempos_de_entrada)
puerta_ganadora = tiempos_de_entrada.index(min_valor) + 1

print(puerta_ganadora)