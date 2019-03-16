import os
import getpass #Libreria para obtener usuario
import time

def vigilante(archivo_borrado):
    archivo_log = "/tmp/log_proyecto"
    usuario_borron = getpass.getuser()
    fecha_hora = time.strftime("%d/%m/%y %H:%M:%S")
    linea_a_escribir = str(archivo_borrado[1]) + " " + archivo_borrado[0] + " " + usuario_borron + " " + fecha_hora + "\n"
    with open(archivo_log, 'a') as f:
        f.write(linea_a_escribir)

def imprime_archivos(file_list):
    contador = 0

    print("     Tamano                                       Archivo")
    for archivo, tamano in file_list:
        contador += 1
        print(contador, "-", round(convierta_MB(tamano), 2), "MB", archivo)

def convierta_MB(peso):
    return peso/1024/1024

def extrae_archivos(ruta_usuario):
    directorio = ruta_usuario
    dicccionario_archivos = {}

    # r=root, d=directories, f = files
    for r,d,f in os.walk(directorio):
        for file in f:
            archivo = os.path.join(r, file)
            #print(archivo)
            try:
                tamano = os.stat(archivo).st_size
            except:
                break
            else:
                dicccionario_archivos [archivo] = tamano
    lista_archivos = sorted(dicccionario_archivos.items(), reverse=True, key=lambda x: x[1])
    return lista_archivos

#ruta = "C:\\"
#ruta = "/"
#ruta = os.getcwd()
ruta = input("Digite la ruta que desea verificar :")
ruta = ruta.split()[0]

if os.path.exists(ruta):
    listaArchivos = extrae_archivos(ruta)

    seguir_eliminando = True


    while seguir_eliminando:
        los10 = listaArchivos[:10]
        imprime_archivos(los10)

        eliminar = int(input("Digite el numero de archivo que desea eliminar"))

        archivo_a_eliminar = los10[eliminar-1][0]
        print("El archivo a eliminar es : ", archivo_a_eliminar)
        desicion_elimina = input("Esta seguro de esta accion S/N?")
        if desicion_elimina.upper() == "S":
            os.remove(archivo_a_eliminar)
            listaArchivos.remove(los10[eliminar-1])
            vigilante(los10[eliminar-1])
        else:
            print("Archivo no se eliminara")

        multiple_delete = input("Desea seguir eliminando S/N")
        if multiple_delete.upper() == "N":
            seguir_eliminando = False
else:
    print("Ruta inexistente")
