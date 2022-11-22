class nodoArista():

    def __init__(self, info, destino):
        self.info = info
        self.destino = destino
        self.sig = None

class nodoVertice():
    def __init__(self, info):
        self.info = info
        self.sig = None
        self.visitado = False
        self.adyacentes = Arista()

class Grafo():

    def __init__(self, dirigido = True):
        #crea un grafo vacío
        self.inicio = None
        self.dirigido = dirigido
        self.tamanio = 0

class Arista():
    #clase lista de aristas implementación sobre lista
    def __init__(self):
        #crea una lista de aristas vacía
        self.inicio = None
        self.tamanio = 0

def insertar_vertice(grafo, dato):
    nodo = nodoVertice(dato)
    if grafo.inicio is None or grafo.inicio.info > dato:
        nodo.sig = grafo.inicio
        grafo.inicio = nodo
    else:
        ant = grafo.inicio
        act = grafo.inicio.sig
        while act is not None and act.info < nodo.info:
            ant = act
            act = act.sig
        nodo.sig = act
        ant.sig = nodo
    grafo.tamanio +=1

def insertar_arista(grafo, dato, origen, destino):
    #inserta una arista desde el nodo origen hasta el destino
    agregar_arista(origen.adyacentes, dato, destino.info)
    if not grafo.dirigido:
        agregar_arista(destino.adyacentes, dato, origen.info)

def agregar_arista(origen, dato, destino):
    #agrega arista desde el vertice origen al destino
    nodo = nodoArista(dato, destino)
    if origen.inicio is None or origen.inicio.destino > destino:
        nodo.sig = origen.inicio
        origen.inicio = nodo
    else:
        ant = origen.inicio
        act = origen.inicio.sig
        while act is not None and act.destino < nodo.destino:
            ant = act
            act = act.sig
        nodo.sig = act
        ant.sig = nodo
    origen.tamanio += 1

def eliminar_vertice(grafo, clave):
    #Elimina un grafo del vértice y devuelve si lo encuentra
    x = None
    if grafo.inicio.info == clave:
        x = grafo.inicio.info
        grafo.inicio = grafo.inicio.sig
        grafo.tamanio -= 1
    else:
        ant = grafo.inicio
        act = grafo.inicio.sig
        while act is not None and act.info != clave:
            ant = act
            act = act.sig
        if act is not None:
            x = act.info
            ant.sig = act.sig
            grafo.tamanio -= 1
    if x is not None:
        aux = grafo.inicio
        while aux is not None:
            if aux.adyacentes.inicio is not None:
                eliminar_arista(aux.adyacentes, clave)
            aux = aux.sig
    return x

def buscar_vertice(grafo, buscado):
    #devuelve la direccion del elemento buscado
    aux = grafo.inicio
    while aux is not None and aux.info != buscado:
        aux = aux.sig
    return aux

def buscar_arista(vertice, buscado):
    #devuelve la direccion del elemento buscado
    aux = vertice.adyacentes.inicio
    while aux is not None and aux.destino != buscado:
        aux = aux.sig
    return aux

def tamanio(grafo):
    return grafo.tamanio

def grafo_vacio(grafo):
    return grafo.inicio is None

def eliminar_arista(vertice, destino):
    x = None
    if vertice.inicio.destino == destino:
        x = vertice.inicio.info
        vertice.inicio = vertice.inicio.sig
        vertice.tamanio -= 1
    else:
        ant = vertice.inicio
        act = vertice.inicio.sig
        while act is not None and act.destino != destino:
            ant = act
            act = act.sig
        if act is not None:
            x = act.info
            ant.sig = act.sig
            vertice.tamani0 -= 1
    return x

def existe_paso(grafo, origen, destino):
    #Barrido en profundidad del grafo
    resultado = False
    if not origen.visitado:
        origen.visitado = True
        vadyacentes = origen.adyacentes.imicio
        while vadyacentes is not None and not resultado:
            adyacente = buscar_vertice(grafo, vadyacentes.destino)
            if adyacente.info == destino.info:
                return True
            elif not adyacente.visitado:
                resultado = existe_paso(grafo, adyacente, destino)
            vadyacentes = vadyacentes.sig
    return resultado

def adyacentes(vertice):
    aux = vertice.adyacentes.inicio
    while aux is not None:
        print(aux.destino, aux.info)
        aux = aux.sig

def es_adyacente(vertice, destino):
    resultado = False
    aux = vertice.adyacentes.inicio
    while aux is not None and not resultado:
        if aux.destino == resultado:
            resultado = True
        aux = aux.sig
    return resultado

def marcar_no_visitado(grafo):
    #marca todos los vertices del grafo como no visitados
    aux = grafo.inicio
    while aux is not None:
        aux.visitado = False
        aux = aux.sig

def barrido_vertices(grafo):
    #realiza un barrido del grafo mostrabdo sus valores
    aux = grafo.inicio
    while aux is not None:
        print(aux.info)
        aux = aux.sig

def barrido_profundidad(grafo, vertice):
    #barrido en profundidad del grafo
    while vertice is not None:
        if not vertice.visitado:
            vertice.visitado = True
            print(vertice.info)
            adyacentes = vertice.adyacentes.inicio
            while adyacentes is not None:
                adyacente = buscar_vertice(grafo, adyacentes.destino)
                if not adyacente.visitado:
                    barrido_profundidad(grafo, adyacente)
                adyacentes = adyacentes.sig
        vertice = vertice.sig

def barrido_amplitud(grafo, vertice):
    pass

grafo = Grafo()

A_B = Arista()
insertar_vertice(grafo, 1)
insertar_vertice(grafo, 2)
insertar_vertice(grafo, 3)
insertar_arista(grafo, 2, grafo.inicio, grafo.inicio.sig)

barrido_profundidad(grafo, grafo.inicio)


