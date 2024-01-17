""". Modifique el script anterior para solicitar la edad del usuario y imprimir en pantalla la edad
en meses. """

nombre = input("Ingrese su nombre: ")
edad = int(input("Ingrese su edad: "))

edad_en_meses = edad * 12

print(f"El nombre es {nombre}, su edad es {edad} años y en meses son {edad_en_meses}")