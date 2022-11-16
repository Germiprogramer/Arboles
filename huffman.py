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

#nos da un elemento
def buscar_dato(raiz, dato):
    if raiz.info == dato:
        return raiz
    else:
        try:
            
            return buscar_dato(raiz.izquierda, dato)
            
        
        except:
            
            return buscar_dato(raiz.derecha, dato)
            


def codificacion(nodo, raiz):
    cod = ""
    
    while nodo != raiz:
        if nodo == nodo.padre.izquierda:
            cod = cod + "0"       
        elif nodo == nodo.padre.derecha:
            cod = cod + "1"
        else:
            return cod
        nodo = nodo.padre
    return reverse(cod)
    

def dic_codificacion_valores(listanodos):
    dic = {}
    aux = listanodos
    listadatos = []
    for i in range(len(listanodos)):
        listadatos.append(listanodos[i].info)
    raiz = crear_arbol(aux)
        
    for i in range(len(listadatos)):
        nododato = buscar_dato(raiz, listadatos[i])
        cod = codificacion(nododato, raiz)
        dic[listadatos[i]] = cod
    return dic

diccionario = dic_codificacion_valores(listanodos)

#def codificar(diccionario, codigo): 



codigo = "00011"
string = ""

def get_key(val, dic):
    for key, value in dic.items():
        if val == value:
            return key
def longitud_maxima(dic):
    longitud = 0
    for val in dic.values():
        if len(val) > longitud:
            longitud = len(val)
        else:
            pass
    return longitud

print(longitud_maxima(diccionario))

posicion = 0
#for i in range(longitud_maxima(diccionario)):
    #for j in diccionario.keys
    #if codigo(posicion, i) == 
for j in diccionario.keys:
    print(j)

        
















        