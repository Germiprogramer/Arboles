def inorden(raiz):    
    if raiz is not None:
        inorden(raiz.izquierda)  
        print(raiz.probabilidad)
        inorden(raiz.derecha)
    else:
        pass

class nodoHuffman():
    def __init__(self, info, probabilidad):
        self.info = info
        self.derecha = None
        self.izquierda = None
        self.probabilidad = probabilidad
        self.codigo = None
        self.padre = None

diccionario = {"A":0.2, "B":0.3, "C":0.5}

listanodos = [nodoHuffman("A", 0.1), nodoHuffman("B", 0.3), nodoHuffman("C", 0.4), nodoHuffman("D", 0.05), nodoHuffman("E",0.15)]

def bubble_sort(lista: list, length: int = 0) -> list: 
    length = length or len(lista)
    swapped = False
    for i in range(length - 1):
        if lista[i].probabilidad > lista[i + 1].probabilidad:
            lista[i], lista[i + 1] = lista[i + 1], lista[i]
            swapped = True

    return lista if not swapped else bubble_sort(lista, length - 1)

def reverse(input):
    if len(input) <= 1:
        return input
 
    return reverse(input[1:]) + input[0]

def crear_arbol(listanodos):
    aux = listanodos
    while len(aux) >1:
        bubble_sort(aux, len(aux))
        padre = nodoHuffman(None, None)
        padre.izquierda = aux[0]
        padre.derecha = aux[1]
        padre.probabilidad = padre.derecha.probabilidad + padre.izquierda.probabilidad
        aux[0].padre = padre
        aux[1].padre = padre
        aux.append(padre)

        del(aux[0])
        del(aux[0])
        

    raiz = aux[0]
    return raiz

inorden(crear_arbol(listanodos))