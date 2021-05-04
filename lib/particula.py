from lib.algoritmos import distancia_euclidiana 

class Particula:
    def __init__(self, id : int = 0, 
                    origen_x : int = 0, origen_y : int = 0,
                    destino_x : int = 0, destino_y : int = 0,
                    velocidad : int = 0 ,
                    red :int = 0, green :int = 0, blue : int = 0):
        self.__id = id
        self.__origen_x = origen_x
        self.__origen_y = origen_y
        self.__destino_x = destino_x
        self.__destino_y = destino_y
        self.__velocidad = velocidad
        self.__red = red 
        self.__green = green
        self.__blue = blue
        self.__distancia =  distancia_euclidiana(self.__origen_x, self.__origen_y, self.__destino_x, self.__destino_y)

    def __str__(self):
        return (
            f"Id: { self.__id }\nOrigen: { self.__origen_x },{ self.__origen_y}\n" + 
            f"Destino: { self.__destino_x},{ self.__destino_y}\nVelocidad: { self.__velocidad }\n" +
            f"Distancia: {round(self.__distancia,4)}\nColor: rgb({ self.__red },{ self.__green },{ self.__blue })\n"
        )

    @property
    def id(self):
        return self.__id
    
    @property
    def origen_x(self):
        return self.__origen_x

    @property
    def origen_y(self):
        return self.__origen_y

    @property
    def destino_x(self):
        return self.__destino_x

    @property
    def destino_y(self):
        return self.__destino_y

    @property
    def velocidad(self):
        return self.__velocidad

    @property
    def red(self):
        return self.__red

    @property
    def green(self):
        return self.__green
    
    @property
    def blue(self):
        return self.__blue

    @property
    def distancia(self):
        return self.__distancia

    def to_dict(self):
        return {
            "id" : self.__id,
            "origen_x" : self.__origen_x,
            "origen_y" : self.__origen_y,
            "destino_x" : self.__destino_x,
            "destino_y" : self.__destino_y,
            "velocidad" : self.__velocidad,
            "red" : self.__red,
            "green" : self.__green,
            "blue" : self.__blue
        }