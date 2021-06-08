import math 
from queue import PriorityQueue

"""
Funciones y clases auxiliares
"""

infinito = 1e15

def printqueue(arr : PriorityQueue):
    pq = PriorityQueue()
    while not arr.empty():
        x = arr.get()
        pq.put(x)
        print(x)

    return pq
    
class DisjointSet:
    def __init__(self):
        self.elements = []

    def print(self):
        print(self.elements)

    def make_set(self,element):
        for elem in self.elements:
            if element in elem:
                return False
        self.elements.append([element])
        return True

    def find_set(self,element):
        for index,elem in enumerate(self.elements):
            if element in elem:
                return index
        return -1 
    
    def union(self,A,B):
        index_A = self.find_set(A)
        index_B = self.find_set(B)

        self.elements[index_A] += self.elements[index_B]
        self.elements.pop(index_B)

""" Calcula la distancia euclidiana

Devuelve el resultado de la fórmula 

También se le conoce a la fórmula como:
distancia entre dos puntos

Parámetros:
x_1 -- origen_x
y_1 -- origen_y
x_2 -- destino_x
y_2 -- destino_y
"""
def distancia_euclidiana(x_1 : int, y_1 : int, x_2 : int, y_2 : int) -> float:
    return math.sqrt((x_2 - x_1)**2 + (y_2 - y_1)**2)

""" Recorre el grafo en anchura

Devuelve el string correspondiente a la salida
en el orden definido

grafo : Grafo a recorrer
"""
def recorrido_anchura(grafo : dict, origen):
    visitados = []
    cola = []
    recorrido = []

    visitados.append(origen)
    cola.append(origen)

    while cola:
        vertice = cola[0]                   #Obtener y eliminar por separado
        recorrido.append(vertice)
        cola.pop(0)

        adyacentes = grafo.get(vertice)

        for ady in adyacentes:             
            ady = ady[0]                    #Obtener destino solamente
            if ady not in visitados:
                visitados.append(ady)
                cola.append(ady)

    return recorrido

""" Recorre el grafo en profundidad

Devuelve el string correspondiente a la salida
en el orden definido

grafo : Grafo a recorrer
"""
def recorrido_profundidad(grafo : dict, origen):
    visitados = []
    pila = []
    recorrido = []

    visitados.append(origen)
    pila.append(origen)

    while pila:
        vertice = pila.pop()                #Retorna y elimina el elemento
        recorrido.append(vertice)

        adyacentes = grafo.get(vertice)

        for ady in adyacentes:              
            ady = ady[0]                    #Obtener destino solamente
            if ady not in visitados:
                visitados.append(ady)
                pila.append(ady)

    return recorrido

"""
Algoritmo de Prim para obtener el arbol de 
expansión mínimo a partir de un origen

Parámetros:
grafo : Grafo del cual obtener el camino
origen : origen del cual vamos a partir
"""
def prim(grafo : dict, origen):
    visitados = []
    pq = PriorityQueue()
    arbol_expansion = []

    visitados.append(origen)

    for ady in grafo.get(origen):
        arista = (ady[1],origen,ady[0])         #Orden peso, origen, destino
        pq.put(arista)               

    while not pq.empty():
        arista = pq.get()
        destino = arista[2]

        if destino not in visitados:
            visitados.append(destino)

            for ady in grafo.get(destino):
                if ady[0] not in visitados:
                    adyacente = (ady[1],destino,ady[0])
                    pq.put(adyacente)
            
            arbol_expansion.append(arista)

    return arbol_expansion 

"""
Algoritmo de Kruskal para obtener el arbol de 
expansión mínimo

Parámetros:
grafo : Grafo del cual obtener el camino
"""
def kruskal(grafo : dict):
    arbol_expansion = []
    ds = DisjointSet()
    lista = PriorityQueue()

    for nodo in grafo:
        for ady in grafo.get(nodo):
            arista = (ady[1] * -1 , nodo, ady[0])     #*-1 para ordenar de mayor a menor
            lista.put(arista)

        ds.make_set(nodo)

    ds.print()

    while not lista.empty():
        arista = lista.get()

        origen = arista[1]
        destino = arista[2]

        if ds.find_set(origen) != ds.find_set(destino):
            arbol_expansion.append(arista)
            ds.union(origen,destino)

            print(f"Arista = {arista}")    
            ds.print()

    return arbol_expansion

"""
Algoritmo de Dijkstra para obtener el camino
más corto a partir de un grafo

Parámetros:
grafo : Grafo del cual obtener el camino
origen : origen del cual vamos a partir

Regresa:
Arreglo de distancias, Arreglo de camino
"""
def dijkstra(grafo : dict, origen):
    distancias = dict()
    camino = dict()
    lista = PriorityQueue()

    for nodo in grafo:
        if nodo == origen:
            distancias[nodo] = 0
            camino[nodo] = origen
        else:
            distancias[nodo] = infinito
            camino[nodo] = ()

    lista.put((0,origen))

    while not lista.empty():
        elemento = lista.get()
        nodo = elemento[1]      

        for arista in grafo[nodo]:
            distancia = arista[1] + elemento[0]     #Distancia al destino + distancia del elemento
            destino = arista[0]

            if distancia < distancias[destino]:
                distancias[destino] = distancia
                camino[destino] = nodo
                lista.put((distancia, destino))

    return distancias, camino


