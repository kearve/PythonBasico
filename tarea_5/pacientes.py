import time

class Paciente():
    def __init__(self, id, nombre, apellido, telefono, direccion):
        self.id = id
        self.nombre = nombre
        self.apellido = apellido
        self.telefono = telefono
        self.direccion = direccion
        self.enfermedades = set()
        self.medicamentos = set()

    def agrega_Enfermdedad(self,enfermedad):
        self.enfermedades.add(enfermedad)

    def agrega_Medicamento(self,medicamento):
        self.medicamentos.add(medicamento)

def opciones(opcion):
    contador = 0

    if opcion == 1: #AGREGAR PACIENTE
        print("******* Informacion del PACIENTE ********")
        cedula = input("Identificacion : ")
        nombre = input("Nombre : ")
        apellido = input("Apellido : ")
        telefono = input("Telefono : ")
        direccion = input("Direccion : ")

        paciente = Paciente(cedula, nombre, apellido, telefono, direccion)
        pacientes_Dict[cedula] = paciente

    elif opcion == 2: #BORRADO PACIENTE
        print("***** Borrado del PACIENTE *****")
        cedula = input("Identificacion del paciente a eliminar: ")
        del pacientes_Dict[cedula]

    elif opcion == 3: #AGREGAR ENFERMEDAD
        print("***** AGREGAR ENFERMDEDAD del PACIENTE *****")
        cedula = input("Identificacion del paciente : ")
        paciente = pacientes_Dict[cedula]

        enfermedad = input("Enfermedad del paciente : ")
        paciente.agrega_Enfermdedad(enfermedad)
        pacientes_Dict[cedula] = paciente

    elif opcion == 4: #AGREGAR MEDICAMENTO
        print("***** AGREGAR MEDICAMENTOS del PACIENTE *****")
        cedula = input("Identificacion del paciente : ")
        paciente = pacientes_Dict[cedula]

        medicamento = input("Medicamento del paciente : ")
        paciente.agrega_Medicamento(medicamento)
        pacientes_Dict[cedula] = paciente

    elif opcion == 5: #REPORTE ENFERMEDADES
        print("*** ENFERMEDADES tratadas ******")
        enfermedades = set()
        pacientes = pacientes_Dict.values()
        for paciente in pacientes:
            for valor in paciente.enfermedades:
                enfermedades.add(valor)

        print(enfermedades)

    elif opcion == 6: #REPORTE MEDICAMENTOS
        print("*** MEDICAMENTOS usados en la clinica ******")
        medicamentos = set()
        pacientes = pacientes_Dict.values()
        for paciente in pacientes:
            for valor in paciente.medicamentos:
                medicamentos.add(valor)

        print(medicamentos)

    elif opcion == 7: #COMPARA PACIENTES
        print("***** COMPARA 2 PACIENTES *****")
        cedula = input("Identificacion del paciente 1 : ")
        paciente_a = pacientes_Dict[cedula]

        cedula = input("Identificacion del paciente 2 : ")
        paciente_b = pacientes_Dict[cedula]

        print("Enfermedades en Comun")
        print(paciente_a.enfermedades & paciente_b.enfermedades)

        print("Enfermedades Diferentes")
        print("Enfermdedades presentes en Paciente 1 pero no en Paciente 2 :",
              paciente_a.enfermedades - paciente_b.enfermedades)
        print("Enfermdedades presentes en Paciente 2 pero no en Paciente 1 :",
              paciente_b.enfermedades - paciente_a.enfermedades)

        print("Medicamentos en Comun")
        print(paciente_a.medicamentos & paciente_b.medicamentos)

        print("Medicamentos Diferentes")
        print("Medicamentos presentes en Paciente 1 pero no en Paciente 2 :",
              paciente_a.medicamentos - paciente_b.medicamentos)
        print("Medicamentos presentes en Paciente 2 pero no en Paciente 1 :",
              paciente_b.medicamentos - paciente_a.medicamentos)
    time.sleep(3)


pacientes_Dict = {}
opcion = "0"

Pedro = Paciente("1", "Pedro", "Carmona", "111111", "Heredia")
Pedro.agrega_Medicamento("pastillas")
Pedro.agrega_Medicamento("inyecccion")
Pedro.agrega_Medicamento("supositorio")
Pedro.agrega_Enfermdedad("colesterol")
Pedro.agrega_Enfermdedad("trigliceridos")
pacientes_Dict["1"] = Pedro

Mario = Paciente("1", "Mario", "Bros", "22222222", "Cartago")
Mario.agrega_Medicamento("pastillas")
Mario.agrega_Medicamento("inyecccion")
Mario.agrega_Medicamento("curita")
Mario.agrega_Enfermdedad("colesterol")
Mario.agrega_Enfermdedad("presion")
pacientes_Dict["2"] = Mario

while opcion != 8:
    print("Que accion desea realizar?")
    print("")
    print("1- Agregar Paciente")
    print("2- Borrar Paciente")
    print("3- Agregar Enfermedad")
    print("4- Agregar Medicamentos")
    print("5- Reporte Enfermedades")
    print("6- Reporte Medicamentos")
    print("7- Compara pacientes")
    print("8- SALIR")
    opcion = int(input("Opcion: "))
    if opcion > 0 and opcion < 8:
        opciones(opcion)
    elif opcion == 8:
        pass
    else:
        print("Opcion incorrecta")


#
# Agregar - Borrar Paciente
# Agregar Enfermedad
# Agregar Medicamento
# Reporte Enfermedad(es)
# Reporte Medicamento(s)
# Compararar 2 pacientes. Enfermedades en Comun, Diferentes. Medicamentos en Comun,Difentes
