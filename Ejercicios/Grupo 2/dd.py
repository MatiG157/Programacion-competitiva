entraces = int(input())

lista = []

lista = list((map(int, input().split())))

""" for i in range(len(lista)):
    if lista[i] / (i+1) < 1:
        print(i)
        break """

""" cont = 0
flag = True

while flag == True:
    for i in range(len(lista)):
        if lista[i] <= (i+cont*len(lista)+1):
            print(i+1)
            flag = False   
            break  
 """


sol = 0
for i in range(len(lista)):
    num = lista[i] / (i+1)
    if (num < sol and lista[i] < guar1) or sol == 0:
        sol = num
        guar1 = lista[i]
        guardar = i+1

print(guardar)