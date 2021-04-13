import math 

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