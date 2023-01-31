class figuraGeometrica:
    def __init__(self, ancho, alto):
        self.__ancho = ancho
        self.__alto = alto
    def alto(self):
        return self.__alto
    def alto(self, alto):
        self.__alto = alto
    def ancho(self):
        return self.__ancho
    def ancho(self, ancho):
        self.__ancho = ancho
    def __str__(self) -> str:
        return f"La figura Geometrica tiene de alto: {self.__alto}, y de ancho {self.__ancho} "
figura1 = figuraGeometrica(4,2)
print(figura1)
    