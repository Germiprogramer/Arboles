class nodoArbol():
    def __init__(self, info):
        self.info = info
        self.derecha = None
        self.izquierda = None
        self.padre = None

def arbol_vacio(raiz):
    return raiz is None

def insertarnodo(raiz, dato):
    if raiz == None:
        print("el nodo es la raiz")
        raiz = nodoArbol(dato)
    else:

        while True:
            if dato<raiz.info:
                if raiz.izquierda is None:
                    raiz.izquierda = nodoArbol(dato)
                    raiz.izquierda.padre = raiz
                    break
                else:
                    raiz = raiz.izquierda
            else:
                if raiz.derecha is None:
                    raiz.derecha = nodoArbol(dato)
                    raiz.derecha.padre = raiz
                    break
                else:
                    raiz = raiz.derecha


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

#desde abajo
def postorden(raiz):
    if raiz is not None:
        postorden(raiz.izquierda)
        postorden(raiz.derecha)
        print(raiz.info)





                