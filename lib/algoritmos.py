import math 
from queue import PriorityQueue

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
Algoritmo de Prim
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

# def printqueue(arr : PriorityQueue):
#     pq = PriorityQueue()
#     while not arr.empty():
#         x = arr.get()
#         pq.put(x)
#         print(x)

#     return pq
    