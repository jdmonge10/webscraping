"""Escriba un script que añada al archivo generado: “Fin del archivo”"""

nombre_archivo = "datos_usuario.txt"

try:
    with open(nombre_archivo, 'r') as archivo:
        contenido = archivo.read()

    contenido += "\nFin del archivo"

    with open(nombre_archivo, 'w') as archivo:
        archivo.read(contenido)

