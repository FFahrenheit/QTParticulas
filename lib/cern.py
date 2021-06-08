from lib.particula import Particula
import json
import lib.algoritmos as alg

class CERN:
    def __init__(self):
        self.__particulas = []

    def agregar_final(self, particula : Particula):
        self.__particulas.append(particula)

    def agregar_inicio(self, particula : Particula):
        self.__particulas.insert(0,particula)

    def mostrar(self):
        for particula in self.__particulas:
            print(particula)

    def __str__(self):
        return "".join(
            str(particula) + '\n' for particula in self.__particulas 
        )

    def __len__(self):
        return len(self.__particulas)
    
    def __iter__(self):
        self.cont = 0

        return self

    def __next__(self):
        if self.cont < len(self.__particulas):
            particula = self.__particulas[self.cont]
            self.cont += 1
            return particula
        else:
            raise StopIteration

    def guardar(self, ubicacion):
        try:
            with open(ubicacion,'w') as archivo:
                lista = [particula.to_dict() for particula in self.__particulas]
                print(lista)
                json.dump(lista, archivo, indent=5)
            return True
        except:
            return False

    def abrir(self, ubicacion):
        try:
            with open(ubicacion, 'r') as archivo:
                lista = json.load(archivo)
                self.__particulas = [Particula(**particula) for particula in lista ]
            return True
        except:
            return False 

    def sort_by_id(self):
        self.__particulas.sort(key=lambda particula : particula.id)

    def sort_by_distancia(self):
        self.__particulas.sort(key=lambda particula : particula.distancia, reverse=True)
    
    def sort_by_velocidad(self):
        self.__particulas.sort(key=lambda particula : particula.velocidad)

    def to_dict(self, parameter='distancia'):
        grafo = dict()
        for particula in self.__particulas:

            key = ( particula.origen_x, particula.origen_y )
            weight = int(particula.distancia) if parameter == 'distancia' else particula.velocidad
            value = ( (particula.destino_x , particula.destino_y ), weight)

            if key in grafo:
                grafo[key].append(value)
            else:
                grafo[key] = [ value ]

            key = ( particula.destino_x, particula.destino_y )
            weight = int(particula.distancia) if parameter == 'distancia' else particula.velocidad
            value = ( (particula.origen_x, particula.origen_y), weight)

            if key in grafo:
                grafo[key].append(value)
            else:
                grafo[key] = [ value ]
            
        self.grafo = grafo
        return self.grafo

    def recorrido_anchura(self,origen):
        recorrido = alg.recorrido_anchura(self.grafo,origen)
        return self.str_recorrido(recorrido)

    def recorrido_profundidad(self,origen):
        recorrido = alg.recorrido_profundidad(self.grafo,origen)
        return self.str_recorrido(recorrido)

    def str_recorrido(self,recorrido):
        out = ""
        for vertice in recorrido:
            out += str(vertice) + '\n'
        
        return out
    
    def prim(self,origen):
        return alg.prim(self.grafo,origen)

    def kruskal(self):
        dict_grafo = self.to_dict('velocidad')
        return alg.kruskal(dict_grafo)

    def dijkstra(self, origen):
        return alg.dijkstra(self.grafo, origen)
        