from Alfabeto import Alfabeto
from Lenguaje import Lenguaje

class Command():
    def ejecutar(self):
        pass

class CommandSimple(Command):

    def __init__(self, objeto):

        self.__objeto = objeto

    def commandObtenerDatos(self):

        if (type(self.__objeto) == Alfabeto):

            return self.__objeto.getSimbolos()

        elif (type(self.__objeto) == Lenguaje):

            return self.__objeto.getPalabras()

    def commandUnion(self, objeto):

        if (type(self.__objeto) == Alfabeto or type(self.__objeto == Lenguaje)):

            return self.__objeto.union(objeto)

    def commandDiferencia(self, objeto):

        if (type(self.__objeto) == Alfabeto or type(self.__objeto == Lenguaje)):

            return self.__objeto.diferencia(objeto)

    def commandInterseccion(self, objeto):

        if (type(self.__objeto) == Alfabeto or type(self.__objeto == Lenguaje)):

            return self.__objeto.interseccion(objeto)

    def commandCerraduraEstrella(self, numero):

        if (type(self.__objeto) == Alfabeto):

            return self.__objeto.cerraduraEstrella(numero)

    def commandConcatenacion(self, objeto):

        if (type(self.__objeto) == Lenguaje):

            return self.__objeto.concatenacion(objeto)

    def commandPotenciacion(self, numero):

        if (type(self.__objeto) == Lenguaje):

            return self.__objeto.potenciacion(numero)

    def commandInversa(self):

        if (type(self.__objeto) == Lenguaje):

            return self.__objeto.inversa()

    def commandCardinal(self):

        if (type(self.__objeto) == Lenguaje):

            return self.__objeto.cardinal()
