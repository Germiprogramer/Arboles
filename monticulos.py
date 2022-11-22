class Heap():
    def __init__(self,tamanio):
        self.tamanio = 0
        self.vector = [None] * tamanio

def agregar(heap, dato):
    heap.vector[heap.tamanio] = dato
    flotar(heap, heap.tamanio)
    heap.tamanio += 1

def quitar(heap):
    intercambio(heap.vector, 0, heap.tamanio-1)
    dato = heap.vector[heap.tamanio]
    heap.tamanio =-1
    hundir(heap, 0)
    return dato

def cantidad_elementos(heap):
    return heap.tamanio

def heap_vacio(heap):
    return heap.tamanio == 0

def heap_lleno(heap):
    return heap.tamanio == len(heap.vector)

def flotar(heap, indice):
    #flota el elemento a la posicion indice
    while (indice>0 and heap.vector[indice]> heap.vector[(indice-1)//2]):
        padre = (indice-1)//2
        intercambio(heap.vector, indice, padre)
        indice = padre

def intercambio(list1, index1, index2):
    list1[index1],list1[index2]=list1[index2],list1[index1]

def hundir(heap, indice):
    hijo_izquierdo = (indice*2)+1
    control = True
    while control and hijo_izquierdo < heap.tamanio:
        hijo_derecho = hijo_izquierdo +1
        aux = hijo_izquierdo
        if hijo_derecho<heap.tamanio:
            if heap.vector[hijo_derecho] > heap.vector[hijo_izquierdo]:
                aux = hijo_derecho
        if heap.vector[indice] < heap.vector[aux]:
            intercambio(heap.vector, indice, aux)
            indice = aux
            hijo_izquierdo= (indice * 2)+1
        else:
            control = False

def monticulizar(heap):
    #Transforma un vector en un monticulo
    for i in range(len(heap.vector)):
        flotar(heap, i)

monticulo = Heap(8)
agregar(monticulo, 10)
agregar(monticulo,7)
agregar(monticulo, 5)
agregar(monticulo, 11)
quitar(monticulo)
#print(monticulo.vector)

#colas y monticulos

def arribo(heap, dato, prioridad):
    #arriba a un elemento a la cola utilizando prioridad
    agregar_cola(heap, [prioridad, dato])

def atencion(heap):
    #atiende al elemento al frente de la cola y lo devuelve
    return quitar(heap)[0]

def agregar_cola(heap, dato):
    heap.vector[heap.tamanio] = dato
    if heap.tamanio>0:
        flotar_cola(heap, heap.tamanio)
    heap.tamanio += 1

def flotar_cola(heap, indice):
    #flota el elemento en la posicion del indice
    i = indice-1
    print(heap.vector)
    
    while True:
        print(heap.vector[i][0])
        if (heap.vector[indice][0]> heap.vector[i][0] and i >0):
            intercambio(heap.vector, indice, i)
            i -=1   
        else:
            break

def cambiar_prioridad(heap, indice, prioridad):
    #cambia la prioridad de un elemento y lo acomoda en el monticulo
    prioridad_anterior = heap[indice][0]
    heap[indice][0] = prioridad
    if prioridad > prioridad_anterior:
        flotar(heap, indice)
    elif(prioridad< prioridad_anterior):
        hundir(heap, indice)

monti = Heap(8)
arribo(monti, 4, 1)
arribo(monti, 6, 3)
arribo(monti, 2, 5)
arribo(monti, 7, 2)
arribo(monti, 1, 4)
print(monti.vector)

from random import randint

heap = Heap(10)

while(not heap_lleno(heap)):
    num = randint(0, 500)
    prioridad = randint(1,3)
    agregar(heap, [prioridad, num])
print(heap.vector)




    

