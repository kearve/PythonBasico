# Tarea 6-A: Monólogo de personas
# Usando el archivo tipo csv -el que está en ese enlace- escribir un código en Python que implemente lo siguiente:
#
# Guardar en un único archivo llamado reporte.txt una frase por persona que exprese lo siguiente:
#
# 'Hola me llamo -el nombre- -el apellido-. Mi teléfono es -el número de teléfono-' .Mi usuario de correo es: -el usuario- usando una cuenta de -nombre del proveedor-'
#
# Por ejemplo; Hola me llamo Erick Salas. Mi teléfono es 83145-7878. Mi usuario de correo es: ericksc usando una cuenta de gmail
#
# Consideraciones:
#
# Para cada una de las personas que están en el archivo csv.
# Por cada reglón del archivo csv, que representa información personal de una colección de individuos.
# El archivo reporte.txt es uno solo, único. Debe contener todos los mensajes de todas las personas.
#
#
### File Located: C:\Users\karrietx\Documents\us-500.csv in my case
#first_name	last_name	company_name	address	city	county	state	zip	phone1	phone2	email	web

import csv

archivo_entrada=r"C:\Users\karrietx\Documents\us-500.csv"
archivo_salida=r"C:\Users\karrietx\Documents\salida.txt"

with open(archivo_entrada, "r") as file:
    reader = csv.reader(file)
    encabezado = True
    with open(archivo_salida, "a") as salida:

        for linea in reader:
            if encabezado == False:
                nombre = linea[0]
                apellido = linea[1]
                telefono1 = linea[8]
                telefono2 = linea[9]
                #Toma la columna 10 del correo y la procesa para tomar el usuario y el dominio
                arroba_located = str(linea[10]).find("@")
                punto_located = str(linea[10]).find(".", arroba_located)
                # usuario = str(linea[10])[0,arroba_located-1]
                # cuenta = str(linea[10])[arroba_located+1,punto_located-1]
                correo = linea[10]
                usuario = correo[0: arroba_located]
                cuenta = correo[arroba_located+1: punto_located]

                salida.write("Hola, me llamo " + nombre + " " + apellido + ". Mi telefono es " + telefono1 + " o " +
                             telefono2 + " .Mi usuario de correo es: " + usuario + "usando una cuenta de " + cuenta +
                             "\n")
            else:
                encabezado = False
