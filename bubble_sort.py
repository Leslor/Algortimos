import random

def buble_sort(lista):
    n=len(lista)
    for i in range(n):
        print(i+1,":",lista)
        cambios=False
        for j in range(0,n-i-1):
            if lista[j]>lista[j+1]:
                lista[j],lista[j+1]= lista[j+1],lista[j]
                cambios=True
        if not cambios:
            break

lista=[random.randint(1,20) for i in range(10) ]
buble_sort(lista)
