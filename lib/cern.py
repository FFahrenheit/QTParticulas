from lib.particula import Particula
import json

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

    def to_dict(self):
        grafo = dict()
        for particula in self.__particulas:

            key = ( particula.origen_x, particula.origen_y )
            value = ( particula.destino_x , particula.destino_y , round(particula.distancia))

            if key in grafo:
                grafo[key].append(value)
            else:
                grafo[key] = [ value ]

            key = ( particula.destino_x, particula.destino_y )
            value = ( particula.origen_x, particula.origen_y, round(particula.distancia))

            if key in grafo:
                grafo[key].append(value)
            else:
                grafo[key] = [ value ]
            
        return grafo

# p1 = Particula(1,10,10,30,35,100,255,255,0)
# p2 = Particula(2,0,0,-10,-20,10,128,128,128)
# p3 = Particula(3,-10,5,0,15,200,92,29,102)

# cern = CERN()
# cern.agregar_final(p1)
# cern.agregar_final(p2)
# cern.agregar_inicio(p3)

# cern.mostrar()