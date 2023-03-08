from Operaciones import Operaciones
import random

class Alfabeto(Operaciones):

    def __init__(self, simbolos):

        self.__simbolos = simbolos

    def getSimbolos(self):

        return self.__simbolos

    def union(self, alfabeto):

        if self.__simbolos | alfabeto.getSimbolos():

            return self.__simbolos | alfabeto.getSimbolos()

        else:

            return "{}"


    def diferencia(self, alfabeto):

        if self.__simbolos - alfabeto.getSimbolos():

            return self.__simbolos - alfabeto.getSimbolos()

        else:

            return "{}"

    def interseccion(self, alfabeto):

        if self.__simbolos & alfabeto.getSimbolos():

            return self.__simbolos & alfabeto.getSimbolos()

        else:

            return "{}"

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

    def cerraduraEstrella(self, numero):

        listaPalabras = set()

        while (len(listaPalabras) != numero):

            longitudPalabra = random.randint(1, 10)
            palabra = ""

            for i in range(0, longitudPalabra):

                palabra += random.choice(list(self.__simbolos))

            listaPalabras.add(self.__comprobar(palabra))

        return listaPalabras
