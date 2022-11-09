class nodoArbol():
    def __init__(self, info):
        self.info = info
        self.derecha = None
        self.izquierda = None

def insertarnodo(raiz, dato):
    if raiz == None:
        print("el nodo es la raiz")
        raiz = nodoArbol(dato)
    else:
        while raiz.info!= dato:
            if raiz.info <= dato and raiz.derecha == None:
                raiz.derecha = nodoArbol(dato)
                print("a")
            elif raiz.info <= dato and raiz.derecha != None:
                raiz = raiz.derecha
                print("b")
            elif raiz.info > dato and raiz.izquierda == None:
                raiz.izquierda = nodoArbol(dato)
                print("c")
            elif raiz.info > dato and raiz.izquierda != None:
                raiz = raiz.izquierda
                print("d")

def inorden(raiz):    
    if raiz is not None:
        inorden(raiz.izquierda)  
        print(raiz.info)
        inorden(raiz.derecha)
    else:
        pass

raiz = nodoArbol(2)
print("-")
insertarnodo(raiz, 4)
print("-")
insertarnodo(raiz,5)
#insertarnodo(raiz,1)
#insertarnodo(raiz,0)

inorden(raiz)




                