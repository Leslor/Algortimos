import random
def busqueda_binaria(lista, numero, low, high):
    if low>high:
        return False
    media =(low+high)//2
    
    if numero==lista[media]:
        
        return True
        
    elif numero<lista[media]:
        return busqueda_binaria(lista, numero, low, media-1)
    
    else:
        return busqueda_binaria(lista, numero, media+1, high)

if __name__=='__main__':
    lista=[random.randint(0,100) for i in range (10)]
    lista.sort()
    print(lista)
    numero=int(input('Ingres un numero del 0 al 100: '))
    resultado=busqueda_binaria(lista, numero, 0, len(lista)-1)

    if resultado:
        print('El numero {} esta en la lista'.format(numero))
    else:
        print('El numero {} no esta en la lista'.format(numero))



    