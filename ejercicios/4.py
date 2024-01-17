"""Genere un script que permita volcar a pantalla el contenido del archivo generado en el
ejercicio anterior. """

nombre_archivo = "datos_usuario.txt"

try:
    with open(nombre_archivo, 'r') as archivo:
        contenido = archivo.read()

        print("Contenido del archivo:")
        print(contenido)

except FileNotFoundError:
    print("ERROR: El archivo {nombre_archivo} no fue encontrado")


