# Preguntas comunes de Python
# Responder las preguntas de manera directa utilizando ejemplos.
#
print("1- Cuáles son las diferencias en la lista y la tupla?")
lista = [1,2,3,4,5]
tupla = (1,2,3,4,5)

print("Lista :", lista)
print("Tupla :", tupla)

lista[1] = "*"
try:
    tupla[1] = "*"
except:
    print("Tupla es inmutable no se puede modificar un valor ")

print("Lista :", lista)
print("Tupla :", tupla)

print("*****************************************************")
print("2- Cómo se puede usar expresiones if else en una sóloa línea, comúnmente llamadas operaraciones ternarias")
bandera = False
resultado = "Verdadero" if bandera == True else "FALSO"
print(resultado)

print("*****************************************************")
print("3- Para que sirve dir() y help()?")
print("dir() Imprime los metodos disponibles en este ejemplo de la variable bandera \n", dir(bandera))
print("help() Imprime la ayuda de python similar al man de linux")
help(list)

print("*****************************************************")
print("4- Que son diccionarios?")
diccionario = {1: "uno", 2: "dos", 3: "tres"}
print(diccionario[1])
print("Es una lista que tiene asociado un key para su acceso")

print("*****************************************************")
print("5- Que son *args y **kwargs ? Como se usan?")
class Humano(object):
    def __init__(self,*args,**kwargs):
        self.nombre = args[0]
        self.apellido = args[1]
        self.datos = kwargs

Kenneth = Humano("Kenneth", "Arrieta", cedula=113200441, email="kearve@gmail.com")
print(Kenneth.nombre, Kenneth.apellido, Kenneth.datos)
print("args Guarda datos y kwags define datos y variables ")

print("*****************************************************")
print("6- Qué son índices negativos?")
fibonacci = [0, 1, 1, 3, 5]
print(fibonacci)
print("Acceso a la ultima posicion usando negativo, recorro en reversa :", fibonacci[-1])

print("*****************************************************")
print("7- Como se puede order aleatoriamente -o desordenar- una lista?")
import random

lista = [[x] for x in range(10)]
random.shuffle(lista)
print(lista)
print("*****************************************************")
print("8- Como se puede ordenar una lista ?")
lista.sort()
print(lista)

print("*****************************************************")
print("9- Explique o justifique los resultados de A0,A1,A2,A3,A4,A5,A6 ?")

A0 = dict(zip(('a','b','c','d','e'),(1,2,3,4,5)))
A1 = range(10)
A2 = sorted([i for i in A1 if i in A0])
A3 = sorted([A0[s] for s in A0])
A4 = [i for i in A1 if i in A3]
A5 = {i:i*i for i in A1}
A6 = [[i,i*i] for i in A1]
print("zip crea los pares y dic lo convierte en diccionario\nA0 :", A0,
      "\nGenera rango de 0 a 9\nA1 :", A1,
      "\nBusca las llaves del diccionario A0 pero no encuentra al ser letras y realice busqueda por numero \nA2 :", A2,
      "\nOrdena los VALORES de A0 \nA3 :", A3,
      "\nImprime los valores del 0 al 9 que se encuentra en A3 \nA4 :", A4,
      "\nCrea un diccionario de numero multplicados por si mismos que se encuentren del 0 al 9 \nA5 :", A5,
      "\nCrea una lista de numeros colocando en parejas por la multiplicacion a si mismos \nA6 :", A6)

print("*****************************************************")
print("10- Cómo se pueden generar números aleatorios? enteros y decimales")
random_entero = random.randrange(0, 100)
random_decimal = random.random()
print("Entero :",random_entero, "Decimal :", random_decimal)

print("*****************************************************")
print("Qué es pickling y unpickling?")
import pickle

with open("humano.pickle", "wb") as envia: #Empaqueta los datos en un file.
    pickle.dump(Kenneth, envia, pickle.HIGHEST_PROTOCOL)


with open("humano.pickle", "rb") as recibe: #Desempaqueta los datos solo legible por el destino que lee por clase humano
    Otro_Kenneth = pickle.load(recibe)
print(Otro_Kenneth.nombre, Otro_Kenneth.datos)

print("*****************************************************")
print("Para que sirve la función map, lambda y filter?")

funcion = lambda var1, var2 : var1 + var2 * 9
valor_retorno = funcion(2, 2) # Crea propias ecuaciones
print(valor_retorno)

valor_retorno = list(map(funcion, A3, A3)) # Usa funcion para trabajar iterables
print(valor_retorno)

valor_retorno = list(filter(lambda x: x > 3, A3 )) #Filtra lista de elementos iterables
print(valor_retorno)

print("*****************************************************")
print("Qué es list comprehension, set comprehension y dict comprehension?")
list_comprehension = [par for par in range(100) if par % 2 == 0]
print(list_comprehension)
set_comprehension = {impar for impar in range(100) if impar % 2 != 0}
print(set_comprehension)
dict_comprehension = {par: impar for par in list_comprehension for impar in set_comprehension}
print(dict_comprehension)
