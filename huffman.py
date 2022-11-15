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

listanodos = [nodoHuffman("A", 0.1), nodoHuffman("B", 0.3), nodoHuffman("C", 0.6)]

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
    while len(listanodos) >1:
        bubble_sort(listanodos, len(listanodos))
        padre = nodoHuffman(None, None)
        padre.izquierda = listanodos[0]
        padre.derecha = listanodos[1]
        padre.probabilidad = padre.derecha.probabilidad + padre.izquierda.probabilidad
        listanodos[0].padre = padre
        listanodos[1].padre = padre
        listanodos.append(padre)

        del(listanodos[0])
        del(listanodos[0])
        

    raiz = listanodos[0]
    return raiz

#nos da un elemento
def buscar_dato(raiz, dato):
    if raiz.info == dato:
        return raiz
    else:
        try:
            
            return buscar_dato(raiz.izquierda, dato)
            
        
        except:
            
            return buscar_dato(raiz.derecha, dato)
            


print(buscar_dato(crear_arbol(listanodos), "C").padre)

def codificacion(nodo, raiz):
    cod = ""
    while nodo != raiz:
        if nodo == nodo.padre.izquierda:
            cod = cod + "0"
            print(0)
        elif nodo == nodo.padre.derecha:
            cod = cod + "1"
            print(1)
        else:
            return cod
        nodo = nodo.padre
    return reverse(cod)
    

print(codificacion(buscar_dato(crear_arbol(listanodos), "B"), crear_arbol(listanodos)))
    
















        