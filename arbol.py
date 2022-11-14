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

def reemplazar(raiz):
    #aux es donde guardamos la raiz a reemplazar
    aux = None
    # si no hay raiz derecha, reemplazamos directamente por la raiz izquierda y el arbol sigue funcionando igual
    if raiz.derecha is None:
        aux = raiz
        raiz = raiz.izquierda
    #si hay raiz derecha 
    else: 
        raiz.derecha, aux = reemplazar(raiz.derecha)
    return raiz, aux

#funciona
def eliminar_nodo(raiz, clave):
    x = None
    if raiz is not None:
        if clave < raiz.info:
            raiz.izquierda, x = eliminar_nodo(raiz.izquierda, clave)
        elif clave > raiz.info:
            raiz.derecha, x = eliminar_nodo(raiz.derecha, clave)
        else:
            x = raiz.info
            if raiz.izquierda is None:
                raiz = raiz.derecha
            elif raiz.derecha is None:
                raiz = raiz.izquierda
            else:
                raiz.izquierda, aux = reemplazar(raiz.izquierda)
                raiz.info = aux.info
    #la raiz que ha eliminado y su valor
    return raiz, x

    pass

#en orden de izquierda a derecha
def inorden(raiz):    
    if raiz is not None:
        inorden(raiz.izquierda)  
        print(raiz.info)
        inorden(raiz.derecha)
    else:
        pass

#ramas de izquierda a derecha
def preorden(raiz):
    if raiz is not None:
        print(raiz.info)
        preorden(raiz.izquierda)
        preorden(raiz.derecha)

#contrario a inorden
def postorden(raiz):
    if raiz is not None:
        postorden(raiz.izquierda)
        postorden(raiz.derecha)
        print(raiz.info)

raiz = nodoArbol(2)
print("-")
insertarnodo(raiz, 5)
print("-")
insertarnodo(raiz,4)
insertarnodo(raiz,7)
insertarnodo(raiz,3)
insertarnodo(raiz,1)
insertarnodo(raiz,0)

eliminar_nodo(raiz, 7)

inorden(raiz)
print("_____")
preorden(raiz)
print("_____")
postorden(raiz)




                