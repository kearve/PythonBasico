import random
import math


class Vehiculo():
    def __init__(self, tipo, avance_metros, funcion):
        self.tipo = tipo
        self.avance = avance_metros
        self.funcion = funcion

    def mover(self):
        self.avance += int(self.funcion(genera_random()))
        # print(self.avance)

    def __str__(self):
        return "{} he avanzado {} metros".format(self.tipo, self.avance)

    def __lt__(self, other):
            return self.avance < other.avance


def genera_random():
    numero_random = random.randint(0, 9)
    return numero_random

class Camion(Vehiculo):
    pass

class Tractor(Vehiculo):
    pass

class Sedan(Vehiculo):
    pass

class Bus(Vehiculo):
    pass


if __name__ == "__main__":
    distancia_ganadora = 1000
    camion = Camion("CAMION", 0, lambda a: 2 * (a) + 1)
    tractor = Tractor("TRACTOR", 0, lambda a: math.log(2) * a)
    sedan = Sedan("SEDAN", 0, lambda a: 3 * (a ** 2))
    bus = Bus("BUS", 0, lambda a: 5 * a)

    ganador = False
    vueltas = 0
    corredores = [camion, tractor, sedan, bus]
    while not ganador:
        vueltas += 1

        print("Vuelta #",vueltas,*corredores)
        camion.mover()
        tractor.mover()
        sedan.mover()
        bus.mover()
        if camion.avance > distancia_ganadora or \
                tractor.avance > distancia_ganadora or \
                sedan.avance > distancia_ganadora or \
                bus.avance > distancia_ganadora:
            ganador = True


corredores.sort(reverse=True)

print("Ganador de la carrera :", corredores[0])
print("Segundo lugar :", corredores[1])
print("Tercer Lugar :", corredores[2])
print("Cuarto Lugar", corredores[3])
print("El numero de vueltas realizadas fueron: ", vueltas)
