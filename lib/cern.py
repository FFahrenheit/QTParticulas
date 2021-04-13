from lib.particula import Particula

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

# p1 = Particula(1,10,10,30,35,100,255,255,0)
# p2 = Particula(2,0,0,-10,-20,10,128,128,128)
# p3 = Particula(3,-10,5,0,15,200,92,29,102)

# cern = CERN()
# cern.agregar_final(p1)
# cern.agregar_final(p2)
# cern.agregar_inicio(p3)

# cern.mostrar()