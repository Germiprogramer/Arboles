# 1 = rojo, 0 = negro
from arbol_equilibrado import reemplazar


class nodoArbolRN():
    def __init__(self, info):
        self.padre = None
        self.izquierda = None
        self.derecha = None
        self.info = info
        self.color = 1

def insertar_nodo(raiz, dato):
    ant = None
    act = raiz
    nodo = nodoArbolRN(dato)
    while act is not None:
        ant = act
        if nodo.info < act.info:
            act = act.izquierda
        else:
            act = act.derecha
    nodo.padre = ant
    if ant is None:
        raiz = nodo
    elif nodo.info < ant.info:
        ant.izquierda = nodo
    else:
        ant.derecha = nodo
    raiz = reparar_insertar(nodo)
    return raiz


def reparar_insertar(nodo):
    aux = None
    while (nodo.padre is not None and nodo.padre.color == 1):
        abuelo = nodo.padre.padre
        if abuelo is not None and nodo.padre == nodo.padre.padre.izquierda:
            aux = nodo.padre.padre.derecha
            if aux is not None and aux.color == 1:
                nodo.padre.color = 0
                aux.color = 0
                nodo.padre.padre.color = 1
                nodo = nodo.padre.padre
            elif nodo == nodo.padre.derecha:
                nodo = nodo.padre
                rotar_izquierda(nodo)
            else:
                nodo.padre.color = 0
                nodo.padre.padre.color = 1
                rotar_derecha(nodo.padre.padre)
        elif nodo.padre.padre is not None:
            aux = nodo.padre.padre.izquierda
            if aux is not None and aux.color == 1:
                nodo.padre.color = 0
                aux.color = 0
                nodo.padre.padre.color = 1
                nodo = nodo.padre.padre
            elif nodo == nodo.padre.izquierda:
                nodo = nodo.padre
                rotar_derecha(nodo)
            else:
                nodo.padre.color = 0
                nodo.padre.padre.color = 1
                rotar_izquierda(nodo.padre.padre)
        else:
            nodo = nodo.padre
    if nodo.padre is None:
        nodo.color = 0
    else:
        while nodo.padre is not None:
            nodo = nodo.padre
    return nodo

def rotar_derecha(nodo):
    aux = nodo.izquierda
    nodo.izquierda = aux.derecha

    if aux.derecha is not None:
        aux.derecha.padre = nodo
    aux.padre = nodo.padre

    if nodo.padre is not None:
        if nodo.padre.derecha == nodo:
            nodo.padre.derecha = aux
        else:
            nodo.padre.izquierda = aux
    aux.derecha = nodo
    nodo.padre = aux

def rotar_izquierda(nodo):
    aux = nodo.derecha
    nodo.derecha = nodo.izquierda

    if aux.izquierda is not None:
        aux.izquierda.padre = nodo
    aux.padre = nodo.padre

    if nodo.padre is not None:
        if nodo.padre.izquierda == nodo:
            nodo.padfe.izquierda = aux
        else:
            nodo.padre.derecha = aux

    aux.izquierda = nodo
    nodo.padre = aux

def eliminar_nodo(raiz, clave):
    dato = None
    if raiz is not None:
        aux = raiz
        while aux is not None and aux.info != clave:
            if clave < aux.info:
                aux = aux.izquierda
            else:
                aux = aux.derecha
        if aux is not None:
            dato = aux.info
            x = None
            y = None

            if aux.izquierda is None or aux.derecha is None:
                y = aux
            else:
                y = reemplazar(aux.izquierda)
            if y.izquierda is not None:
                x = y.izquierda
            else:
                x = y.derecha

            if y.padre is not None:
                if y.padre.izquierda is not None and y.padre.izquierda == y:
                    y.padre.izquierda = x
                elif y.padre.derecha is not None and y.padre.derecha == y:
                    y.padre.derecha = x
            if x is None and y.padre is None and y.color ==0:
                x = nodoArbolRN(0)
                x.color = y.color
            if x is not None:
                x.padre = y.padre
            if y != aux:
                aux.info = y.info

            if y.padre is None and y.izquierda is None and y.derecha is None:
                raiz = x
                return raiz,dato
            if y.color == 0:
                aux = reparar_eliminar(x)
                if aux is not None:
                    raiz = aux

    return raiz,dato

def reparar_eliminar(nodo):
    #repara el equilibrio de un dato luego de utilizar un nodo
    while nodo is not None and nodo.padre is not None and nodo.color == 0:
        if nodo == nodo.padre.izquierda or nodo.padre.izquierda is None:
            w = nodo.padre.derecha
            if w.color == 1:
                w.color = 0
                nodo.padre.color = 1
                rotar_izquierda(nodo.padre)
                w = nodo.padre.derecha
            if ((w.izquierda is None and w.derecha is None) or (w.izquierda is not None and w.izquierda.color == 0 and w.derecha is not None and w.derecha.color == 0)):
                w.color = 1
                nodo = nodo.padre
            else:
                if w.derecha.color ==0:
                    w.izquierda.color =0
                    w.color = 1
                    rotar_derecha(w)
                    w = nodo.padre.derecha
                w.color = nodo.padre.color
                nodo.padre.color = 0
                w.derecha.color = 0
                rotar_izquierda(nodo.padre)
            else:
                pass
            #duda como continuar este codigo




    


