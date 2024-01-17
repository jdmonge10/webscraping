"""Modifique el script anterior para guardar los datos del usuario en un archivo de texto."""

nombre = input("Ingrese su nombre: ")
edad = int(input("Ingrese su edad: "))
edad_en_meses = edad * 12

datos_usuario = f"Nombre: {nombre}\n Edad: {edad}\n Edad en Meses: {edad_en_meses}"

nombre_archivo = "datos_usuario.txt"

with open(nombre_archivo, 'w') as archivo:
    archivo.write(datos_usuario)

print(f"Los datos del usuario se han guardado satisfactoriamente en {nombre_archivo}")


