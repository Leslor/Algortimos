import random

def busqueda_binaria(lista,numero, low, high):
    while low<=high:
        media=(low+high)//2
        if lista[media]==numero:
            return media
            return True       
        elif lista[media]>numero:
            high=media-1
        else:
            low=media+1


def run():
    lista = sorted([random.randint(1,10) for i in range (10)])
    numero = int(input('Ingrese numero del 1 al 10: '))
    resultado=busqueda_binaria(lista, numero, 0, len(lista)-1)
    if resultado:
        print('El {} esta en la posicion {}'.format(numero, resultado))
    else:
        print('El {} no esta en la lista'.format(numero))
       
        
if __name__=="__main__":
    run()


