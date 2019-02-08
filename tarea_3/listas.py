import time

opcion = "0"
lista_1 = []
lista_2 = []

def crea_lista():
    lista = []
    cantidad_Palabras = int(input("Ingrese cantidad de palabras que agregara en la lista: "))
    for i in range(cantidad_Palabras):
        print("Digite la palabra #",i+1,":")
        palabra_digitada = input()
        lista.append(palabra_digitada)
    return lista

def opciones(opcion):
    contador = 0
    lista_1 = crea_lista()
    print("La lista #1 digitada es: ",lista_1)

    if opcion == 2:
        buscar = input("Digite la palabra que desea buscar en la lista : ")
        contador = lista_1.count(buscar)       
        print("La palabra :",buscar," aparece ",contador, "vez/veces")
    elif opcion == 3:
        existe = input("Palabra en la lista a modificar: ")
        posicion = lista_1.index(existe)
        reemplazo = input("Digite la palabra a nueva: ")
        if posicion:
            lista_1[posicion] = reemplazo
            print(lista_1)
        else:
            print("Palabra no existe")
    elif opcion == 4:
        existe = input("Palabra que desea eliminar de la lista: ")
        lista_1.remove(existe)
        print(lista_1)
    elif opcion == 5:
        print("La siguiente lista debera contener los nombres que desee eliminar")
        lista_2 = crea_lista()
        print("La lista #2 digitada es: ",lista_2)
        lista_1 = list(set(lista_1) - set(lista_2))
        print("La lista #1 ahora es :",lista_1)
    elif opcion == 6:
        lista_2 = lista_1[::-1]
        print("La nueva lista generada es :",lista_2)
    elif opcion == 7:
        lista_1 = list(set(lista_1))
        print("La lista sin repetidos seria :",lista_1)
    elif opcion == 8:
        print("A continuacion creara la segunda lista")
        lista_2 = crea_lista()
        print("Palabras que aparecen en las 2 listas",list(set(lista_1) & set(lista_2)))
        print("Palabras en la primer lista que no estan en la segunda",list(set(lista_1) - set(lista_2)))
        print("Palabras en la segunda lista que no estan en la primera",list(set(lista_2) - set(lista_1)))
        print("Todas las palabras",set(lista_2 + lista_1))
    time.sleep(3)

while opcion != 9:
    print("Que accion desea realizar?")
    print("")
    print("1- Crear una lista")
    print("2- Busca una palabra")
    print("3- Sustituye palabras")
    print("4- Elimina palabra")
    print("5- Crea 2 listas y elimina palabras")
    print("6- Genera segunda lista viceversa")
    print("7- Elimina repetidos")
    print("8- Coincidencias de listas")
    print("9- SALIR")
    opcion = int(input("Opcion: "))
    if opcion > 0 and opcion < 9:
        opciones(opcion)
    elif opcion == 9:
        pass          
    else:
        print("Opcion incorrecta")
