def inorden(raiz):    
    if raiz is not None:
        inorden(raiz.izquierda)  
        print(raiz.probabilidad)
        inorden(raiz.derecha)
    else:
        pass

class nodoHuffman():
    def __init__(self, info, probabilidad):
        self.probabilidad = info
        self.derecha = None
        self.izquierda = None
        self.probabilidad = probabilidad
        self.codigo = None
        self.padre = None

diccionario = {"A":0.2, "B":0.3, "C":0.5}

listanodos = [nodoHuffman("A", 0.2), nodoHuffman("B", 0.3), nodoHuffman("C", 0.5)]

listanodos[0].padre = nodoHuffman(None, None)
listanodos[1].padre = listanodos[0].padre
listanodos[0].padre.probabilidad = listanodos[0].probabilidad + listanodos[1].probabilidad

padre = nodoHuffman(None, None)
padre.derecha =

inorden(padre)


        