class Animal:
    def __init__(self, nombre, dieta, tamano):
        self.tamanno = tamano
        self.dieta = dieta
        self.nombre = nombre
    def comer(self):
        if self.dieta == "carnivoro":
            print("Buscando presa .....")
            print("Moverse sigilosamente")
            print("Capturar y comer presa")
        elif self.dieta == "herviboro":
            print("Buscando mejor planta")
            print("Comiendo hojas")
        else:
            print ("Buscando lo que sea")
    def dormir(self):
        print("Esta durmiendo")
        print("ZZZZZZZzzzzzzz")


class Planta:
    def __init__(self, nombre, tipo, medicinal):
        self.tipo = tipo
        self.Medicinal = medicinal
        self.nombre = nombre

    def comer(self):
        print("Tomando rayos solares")
        print("Extrayendo nutrientes de la tierra")

    def morir(self):
        print("Tiempo en este mundo agotado ...")


lobo = Animal("LOBO", "carnivoro", "Grande")
koala = Animal("KOALA", "herviboro", "Mediano")
perro = Animal("PERRO","casero","Mediano")


print("=== REINO ANIMAL ==")
print("#########")
print(perro.nombre, perro.dieta)
perro.dormir()
print("#########")
print(lobo.nombre, lobo.tamanno)
lobo.comer()
print("#########")
print(koala.nombre, koala.dieta)
koala.comer()
print("#########")

culantro = Planta("CULANTRO","TIERRA",False)
juanilama = Planta("JUANILAMA","TIERRA", True)

print("=== REINO VEGETAL ==")
print(culantro.nombre,"¿Es medicinal?",culantro.Medicinal)
culantro.comer()
print("#########")
print (juanilama.nombre,"¿Es medicinal?",juanilama.Medicinal)
juanilama.morir()

