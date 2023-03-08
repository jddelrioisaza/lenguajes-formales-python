from Alfabeto import Alfabeto
from Lenguaje import Lenguaje
from Command import CommandSimple

def corregir(simbolos):

    for i in range(0, len(simbolos)):

        if (simbolos[i] == "+++"):

            simbolos[i] = ","

    return simbolos

def menuAlfabeto():

    while True:

        respuesta = input(" -{ALFABETOS}- \n1. CREAR\n2. LISTAR\n3. UNIÓN\n4. DIFERENCIA\n5. INTERSECCIÓN\n6. CERRADURA DE ESTRELLA\n0. RETROCEDER\n¿CUÁL OPCIÓN (NÚMERO) QUIERES ACCEDER?: ")

        if respuesta == "1":

            simbolos = set(corregir(input("¿CUÁLES SON LOS SÍMBOLOS PERTENECIENTES A ESTE ALFABETO?\nPARA USAR LA , COMO SÍMBOLO, USA LA COMBINACIÓN +++\nPARA USAR EL SIMBOLO VACÍO, USA EL CARACTER #\nLOS SÍMBOLOS DEBEN DE ESTAR SEPARADOS POR ,: ").split(",")))
            listaAlfabetos.append(Alfabeto(simbolos))

        elif respuesta == "2":

            if (len(listaAlfabetos) != 0):

                for i in range(0, len(listaAlfabetos)):

                    print(f"ALFABETO N-{i + 1}: {CommandSimple(listaAlfabetos[i]).commandObtenerDatos()}")

            else:

                print("¡NO HAS CREADO NINGÚN ALFABETO!")

        elif respuesta == "3":

            if (len(listaAlfabetos) != 0):

                while True:

                    print(f"TIENES {len(listaAlfabetos)} ALFABETOS")
                    alfabetoA = int(input(f"¿CUÁL ES EL PRIMER ALFABETO (1 - {len(listaAlfabetos)}) CON EL QUE VAS A REALIZAR LA UNIÓN?: ")) - 1
                    alfabetoB = int(input(f"¿CUÁL ES EL SEGUNDO ALFABETO (1 - {len(listaAlfabetos)}) CON EL QUE VAS A REALIZAR LA UNIÓN?: ")) - 1

                    if (alfabetoA >= 0 and alfabetoA < len(listaAlfabetos)) and (alfabetoB >= 0 and alfabetoB < len(listaAlfabetos)):
                        break

                print(f"EL RESULTADO DE LA UNIÓN DE LOS ALFABETOS ES: {CommandSimple(listaAlfabetos[alfabetoA]).commandUnion(listaAlfabetos[alfabetoB])}")

            else:

                print("¡NO HAS CREADO NINGÚN ALFABETO!")

        elif respuesta == "4":

            if (len(listaAlfabetos) != 0):

                while True:

                    print(f"TIENES {len(listaAlfabetos)} ALFABETOS")
                    alfabetoA = int(input(f"¿CUÁL ES EL PRIMER ALFABETO (1 - {len(listaAlfabetos)}) CON EL QUE VAS A REALIZAR LA DIFERENCIA?: ")) - 1
                    alfabetoB = int(input(f"¿CUÁL ES EL SEGUNDO ALFABETO (1 - {len(listaAlfabetos)}) CON EL QUE VAS A REALIZAR LA DIFERENCIA?: ")) - 1

                    if (alfabetoA >= 0 and alfabetoA < len(listaAlfabetos)) and (alfabetoB >= 0 and alfabetoB < len(listaAlfabetos)):
                        break

                print(f"EL RESULTADO DE LA DIFERENCIA DE LOS ALFABETOS ES: {CommandSimple(listaAlfabetos[alfabetoA]).commandDiferencia(listaAlfabetos[alfabetoB])}")

            else:

                print("¡NO HAS CREADO NINGÚN ALFABETO!")

        elif respuesta == "5":

            if (len(listaAlfabetos) != 0):

                while True:

                    print(f"TIENES {len(listaAlfabetos)} ALFABETOS")
                    alfabetoA = int(input(f"¿CUÁL ES EL PRIMER ALFABETO (1 - {len(listaAlfabetos)}) CON EL QUE VAS A REALIZAR LA INTERSECCIÓN?: ")) - 1
                    alfabetoB = int(input(f"¿CUÁL ES EL SEGUNDO ALFABETO (1 - {len(listaAlfabetos)}) CON EL QUE VAS A REALIZAR LA INTERSECCIÓN?: ")) - 1

                    if (alfabetoA >= 0 and alfabetoA < len(listaAlfabetos)) and (alfabetoB >= 0 and alfabetoB < len(listaAlfabetos)):
                        break

                print(f"EL RESULTADO DE LA INTERSECCIÓN DE LOS ALFABETOS ES: {CommandSimple(listaAlfabetos[alfabetoA]).commandInterseccion(listaAlfabetos[alfabetoB])}")

            else:

                print("¡NO HAS CREADO NINGÚN ALFABETO!")

        elif respuesta == "6":

            if (len(listaAlfabetos) != 0):

                while True:

                    print(f"TIENES {len(listaAlfabetos)} ALFABETOS")

                    alfabetoA = int(input(f"¿CUÁL ES EL ALFABETO (1 - {len(listaAlfabetos)}) CON EL QUE VAS A REALIZAR LA CERRADURA DE ESTRELLA?: ")) - 1

                    if (alfabetoA >= 0 and alfabetoA < len(listaAlfabetos)):
                        break

                numeroCerraduraEstrella = int(input("¿CUÁNTAS PALABRAS QUIERES GENERAR?: "))
                print(f"EL RESULTADO DE LA CERRADURA DE ESTRELLA ES: {CommandSimple(listaAlfabetos[alfabetoA]).commandCerraduraEstrella(numeroCerraduraEstrella)}")

            else:

                print("¡NO HAS CREADO NINGÚN ALFABETO!")

        elif respuesta == "0":
            break

        else:

            print("¡NO EXISTE ESA OPCIÓN!")

def menuLenguaje():

    while True:

        respuesta = input(" -{LENGUAJES}- \n1. CREAR\n2. LISTAR\n3. UNIÓN\n4. DIFERENCIA\n5. INTERSECCIÓN\n6. CONCATENACIÓN\n7. POTENCIACIÓN\n8. INVERSA\n9. CARDINAL\n0. RETROCEDER\n¿CUÁL OPCIÓN (NÚMERO) QUIERES ACCEDER?: ")

        if respuesta == "1":

            if (len(listaAlfabetos) != 0):

                while True:

                    print(f"TIENES {len(listaAlfabetos)} ALFABETOS")

                    alfabetoA = int(input(f"¿CUÁL ES EL ALFABETO (1 - {len(listaAlfabetos)}) CON EL QUE VAS A GENERAR EL LENGUAJE?: ")) - 1

                    if (alfabetoA >= 0 and alfabetoA < len(listaAlfabetos)):
                        break

                numeroCerraduraEstrella = int(input("¿CUÁNTAS PALABRAS TENDRÁ EL LENGUAJE?: "))
                listaLenguajes.append(Lenguaje(CommandSimple(listaAlfabetos[alfabetoA]).commandCerraduraEstrella(numeroCerraduraEstrella)))

            else:

                print("¡NO HAS CREADO NINGÚN ALFABETO!")

        elif respuesta == "2":

            if (len(listaLenguajes) != 0):

                for i in range(0, len(listaLenguajes)):

                    print(f"LENGUAJE N-{i + 1}: {CommandSimple(listaLenguajes[i]).commandObtenerDatos()}")

            else:

                print("¡NO HAS CREADO NINGÚN LENGUAJE!")

        elif respuesta == "3":

            if (len(listaLenguajes) != 0):

                while True:

                    print(f"TIENES {len(listaLenguajes)} LENGUAJES")
                    lenguajeA = int(input(f"¿CUÁL ES EL PRIMER LENGUAJE (1 - {len(listaLenguajes)}) CON EL QUE VAS A REALIZAR LA UNIÓN?: ")) - 1
                    lenguajeB = int(input(f"¿CUÁL ES EL SEGUNDO LENGUAJE (1 - {len(listaLenguajes)}) CON EL QUE VAS A REALIZAR LA UNIÓN?: ")) - 1

                    if (lenguajeA >= 0 and lenguajeA < len(listaLenguajes)) and (lenguajeB >= 0 and lenguajeB < len(listaLenguajes)):
                        break

                print(f"EL RESULTADO DE LA UNIÓN DE LOS LENGUAJES ES: {CommandSimple(listaLenguajes[lenguajeA]).commandUnion(listaLenguajes[lenguajeB])}")

            else:

                print("¡NO HAS CREADO NINGÚN LENGUAJE!")

        elif respuesta == "4":

            if (len(listaLenguajes) != 0):

                while True:

                    print(f"TIENES {len(listaLenguajes)} LENGUAJES")
                    lenguajeA = int(input(f"¿CUÁL ES EL PRIMER LENGUAJE (1 - {len(listaLenguajes)}) CON EL QUE VAS A REALIZAR LA DIFERENCIA?: ")) - 1
                    lenguajeB = int(input(f"¿CUÁL ES EL SEGUNDO LENGUAJE (1 - {len(listaLenguajes)}) CON EL QUE VAS A REALIZAR LA DIFERENCIA?: ")) - 1

                    if (lenguajeA >= 0 and lenguajeA < len(listaLenguajes)) and (lenguajeB >= 0 and lenguajeB < len(listaLenguajes)):
                        break

                print(f"EL RESULTADO DE LA DIFERENCIA DE LOS LENGUAJES ES: {CommandSimple(listaLenguajes[lenguajeA]).commandDiferencia(listaLenguajes[lenguajeB])}")

            else:

                print("¡NO HAS CREADO NINGÚN LENGUAJE!")

        elif respuesta == "5":

            if (len(listaLenguajes) != 0):

                while True:

                    print(f"TIENES {len(listaLenguajes)} LENGUAJES")
                    lenguajeA = int(input(f"¿CUÁL ES EL PRIMER LENGUAJE (1 - {len(listaLenguajes)}) CON EL QUE VAS A REALIZAR LA INTERSECCIÓN?: ")) - 1
                    lenguajeB = int(input(f"¿CUÁL ES EL SEGUNDO LENGUAJE (1 - {len(listaLenguajes)}) CON EL QUE VAS A REALIZAR LA INTERSECCIÓN?: ")) - 1

                    if (lenguajeA >= 0 and lenguajeA < len(listaLenguajes)) and (lenguajeB >= 0 and lenguajeB < len(listaLenguajes)):
                        break

                print(f"EL RESULTADO DE LA INTERSECCIÓN DE LOS LENGUAJES ES: {CommandSimple(listaLenguajes[lenguajeA]).commandInterseccion(listaLenguajes[lenguajeB])}")

            else:

                print("¡NO HAS CREADO NINGÚN LENGUAJE!")

        elif respuesta == "6":

            if (len(listaLenguajes) != 0):

                while True:

                    print(f"TIENES {len(listaLenguajes)} LENGUAJES")
                    lenguajeA = int(input(f"¿CUÁL ES EL PRIMER LENGUAJE (1 - {len(listaLenguajes)}) CON EL QUE VAS A REALIZAR LA CONCATENACIÓN?: ")) - 1
                    lenguajeB = int(input(f"¿CUÁL ES EL SEGUNDO LENGUAJE (1 - {len(listaLenguajes)}) CON EL QUE VAS A REALIZAR LA CONCATENACIÓN?: ")) - 1

                    if (lenguajeA >= 0 and lenguajeA < len(listaLenguajes)) and (lenguajeB >= 0 and lenguajeB < len(listaLenguajes)):
                        break

                print(f"EL RESULTADO DE LA CONCATENACIÓN DE LOS LENGUAJES ES: {CommandSimple(listaLenguajes[lenguajeA]).commandConcatenacion(listaLenguajes[lenguajeB])}")

            else:

                print("¡NO HAS CREADO NINGÚN LENGUAJE!")

        elif respuesta == "7":

            if (len(listaLenguajes) != 0):

                while True:

                    print(f"TIENES {len(listaLenguajes)} LENGUAJES")
                    lenguajeA = int(input(f"¿CUÁL ES EL LENGUAJE (1 - {len(listaLenguajes)}) CON EL QUE VAS A REALIZAR LA POTENCIACIÓN?: ")) - 1

                    if (lenguajeA >= 0 and lenguajeA < len(listaLenguajes)):
                        break

                exponente = int(input("¿CUÁNTAS ES EL EXPONENTE AL QUE VAS A ELEVAR EL LENGUAJE?: "))
                print(f"EL RESULTADO DE LA POTENCIACIÓN DEL LENGUAJE ES: {CommandSimple(listaLenguajes[lenguajeA]).commandPotenciacion(exponente)}")

            else:

                print("¡NO HAS CREADO NINGÚN LENGUAJE!")

        elif respuesta == "8":

            if (len(listaLenguajes) != 0):

                while True:

                    print(f"TIENES {len(listaLenguajes)} LENGUAJES")
                    lenguajeA = int(input(f"¿CUÁL ES EL LENGUAJE (1 - {len(listaLenguajes)}) QUE VAS A INVERTIR?: ")) - 1

                    if (lenguajeA >= 0 and lenguajeA < len(listaLenguajes)):
                        break

                print(f"EL RESULTADO DE INVERTIR EL LENGUAJE ES: {CommandSimple(listaLenguajes[lenguajeA]).commandInversa()}")

            else:

                print("¡NO HAS CREADO NINGÚN LENGUAJE!")

        elif respuesta == "9":

            if (len(listaLenguajes) != 0):

                while True:

                    print(f"TIENES {len(listaLenguajes)} LENGUAJES")
                    lenguajeA = int(input(f"¿CUÁL ES EL LENGUAJE (1 - {len(listaLenguajes)}) DEL QUE VAS A SACAR EL CARDINAL?: ")) - 1

                    if (lenguajeA >= 0 and lenguajeA < len(listaLenguajes)):
                        break

                print(f"EL CARDINAL DEL LENGUAJE ES: {CommandSimple(listaLenguajes[lenguajeA]).commandCardinal()}")

            else:

                print("¡NO HAS CREADO NINGÚN LENGUAJE!")

        elif respuesta == "0":
            break

        else:

            print("¡NO EXISTE ESA OPCIÓN!")

def menu():

    while True:

        respuesta = input(" -{MENÚ}- \n1. ALFABETOS\n2. LENGUAJES\n0. SALIR\n¿A CUÁL OPCIÓN (NÚMERO) QUIERES ACCEDER?: ")

        if respuesta == "1":

            menuAlfabeto()

        elif respuesta == "2":

            menuLenguaje()

        elif respuesta == "0":
            break

        else:

            print("¡NO EXISTE ESA OPCIÓN!")

listaAlfabetos = list()
listaLenguajes = list()

menu()
