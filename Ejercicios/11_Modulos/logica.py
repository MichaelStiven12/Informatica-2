'''
Este módulo se llama lógica, mediante el cual se suman tres numeros, se suman n numeros y se suman dos listas elemento a elemento.'''


def sumaDeTresNumeros(numero1,numero2,numero3):
    suma = numero1 + numero2 + numero3
    print(suma)

def sumaDeNNumeros(*numero):
    suman = 0
    for i in numero:
        suman = suman + i
    print(suman)

def sumaDeDosListas(lista1,lista2):
    listasSumadas = []
    for i in range(0,len(lista1)):
        sumal = lista1[i] + lista2[i]
        listasSumadas.append(sumal)
    print(listasSumadas)

