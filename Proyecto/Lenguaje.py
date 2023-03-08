import itertools
from Operaciones import Operaciones

class Lenguaje(Operaciones):

    def __init__(self, palabras):

        self.__palabras = palabras

    def getPalabras(self):

        return self.__palabras

    def union(self, lenguaje):

        return self.__palabras | lenguaje.getPalabras()

    def diferencia(self, lenguaje):

        return set(self.__palabras) - set(lenguaje.getPalabras())

    def interseccion(self, lenguaje):

        return self.__palabras & lenguaje.getPalabras()

    def concatenacion(self, lenguaje):

        respuesta = set()

        for i in self.__palabras:

            for j in lenguaje.getPalabras():

                respuesta.add(self.__comprobar(i + j))

        return respuesta

    def __comprobar(self, palabra):

        bandera = False

        for letra in palabra:

                if letra != "#":

                    bandera = True

        if (bandera == True):

            palabra = palabra.replace("#", "")

        else:

            palabra = "#"

        return palabra

    def potenciacion(self, exponente):

        lista = list(itertools.product(self.__palabras, repeat = exponente))
        resultado = set()

        for i in range(0, len(lista)):

            palabra = ""

            for j in range(0, len(lista[i])):

                palabra += lista[i][j]

            resultado.add(self.__comprobar(palabra))

        return resultado


    def inversa(self):

        lista = list(self.__palabras)

        for i in range(0, len(lista)):

            lista[i] = lista[i][::-1]

        return lista

    def cardinal(self):

        return len(self.__palabras)
