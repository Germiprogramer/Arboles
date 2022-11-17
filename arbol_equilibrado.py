class nodoArbol:
    def __init__(self, info):
        self.izquierda = None
        self.derecha = None
        self.info = info
        self.altura = 0

def altura(raiz):
    if raiz is None:
        return -1
    else:
        return raiz.altura

def actualizar_altura(raiz):
    if raiz is not None:
        altura_izquierda = altura(raiz.izquierda)
        altura_derecha = altura(raiz.derecha)
        raiz.altura = (altura_izquierda if altura_izquierda > altura_derecha else altura_derecha) +1

#control:True    ROTACIÓN DERECHA
def rotar_simple(raiz, control):
    if control:
        aux = raiz.izquierda
        raiz.izquierda = aux.derecha
        aux.derecha = raiz
    else:
        aux = raiz.derecha
        raiz.derecha = aux.izquierda
        aux.izquierda = raiz

def rotar_doble(raiz, control):
    if control:
        raiz.izquierda = rotar_simple(raiz.izquierda, False)
        raiz = rotar_simple(raiz, True)
    else:
        raiz.derecha = rotar_simple(raiz.derecha, True)
        raiz = rotar_simple(raiz, False)
    return raiz

def balancear(raiz):
    if raiz is not None:
        if (altura(raiz.izquierda)-altura(raiz.derecha)) == 2:
            if altura(raiz.izquierda.izquierda) >= altura(raiz.izquierda.derecha):
                raiz = rotar_simple(raiz, True)
            else: 
                raiz = rotar_doble(raiz, True)
        elif(altura)