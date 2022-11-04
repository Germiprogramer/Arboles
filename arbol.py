class nodoArbol():
    def __init__(self, info):
        self.info = info
        self.derecha = None
        self.izquierda = None

def insertarnodo(raiz, dato):
    if raiz == None:
        print("el nodo es la raiz")
        raiz = dato
    else:
        while True:
            if raiz.info <= dato and raiz.derecha == None:
                raiz.derecha = nodoArbol(dato)
            elif raiz.info <= dato and raiz.derecha != None:
                raiz = raiz.derecha
            elif raiz.info > dato and raiz.izquierda == None:
                raiz.izquierda = nodoArbol(dato)
            elif raiz.info > dato and raiz.izquierda != None:
                raiz = raiz.izquierda
        

insertarnodo(None, nodoArbol(2))


                