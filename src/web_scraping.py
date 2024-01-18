# importar el modulo request para extrar una pagina web
import requests
# importar el modulo bs4 la libreria BeautifulSoup para transformar el código en html
from bs4 import BeautifulSoup
# importar módulo datetime para trabajar con fechas y horas
from datetime import datetime

# Definimos la función transformar_fecha con el parámetro fecha_caracteres para transformar las fechas en formato de git cadena de caracteres en formato objeto datetime
def transformar_fecha(fecha_caracteres):
    # Creamos un objeto datetime a partir de fecha_caracteres con 3 argumentos (año, mes y día)
    fecha = datetime(int(fecha_caracteres[0:4]), int(fecha_caracteres[4:6]),
                     int(fecha_caracteres[6:8]))
    # Devolvemos el objeto datetime que hemos creado
    return fecha

# Definimos la función transformar_titulo, mediante el parámetro título, para cambiar el formato
def transformar_titulo(titulo):
    # Del titulo eliminamos las comillas simples y las dobles
    titulo = titulo.replace('\'', '').replace('"', '').replace(',', '')
    # Devolvemos la cadena de caracteres modificada
    return titulo

# Definimos la función webscraping para extraer info de la web de Telemadrid con los parámetros url_scraping (web donde queremos sacar la info) y categoría_scraping (categoría de noticias que queremos extraer), asignando el valor de 'todas' para extraer todas las noticias de la web
def webscraping(url_scraping,categoria_scraping='todas'):
    # URL de telemadrid
    # asginamos a la variable url el valor url_scraping que contiene la url de la página que queremos raspar
    url = url_scraping

    # Realizar la petición
    try:
        #Realizamos la solicitud http get a la url que hemos especificado en la biblioteca requests
        respuesta = requests.get(url)
        #print(respuesta)
        #print(respuesta.text)
        # Verificar si la petición fue exitosa (código 200)
        if respuesta.status_code == 200:
            # # Iniciamos el bloque try para generar una excepción de forma segura
            try:
                # abrimos el archivo 'noticas.csv' en formato escritura usando el contexto with
                with open('../data/noticias.csv', 'w') as f:
                    # escribimos una línea de encabezado en el archivo 'noticias.csv' con la lista de categorías que queremos extraer (título, url, categoría, fecha) y añadimos un salto de línea con '\n'
                    f.write('titulo,url,categoria,fecha'+'\n')
                # Analizar el contenido con BeautifulSoup
                # excepto:
            except:
                # en caso de no poderse crear el archivo, saltará el siguiente error
                print("ERROR: no se pudo crear el archivo noticias.csv")
            # # Iniciamos el bloque try para genera una excepción de forma segura
            try:
                # usamos BeautifulSoup para analizar el contenido HTML de la respuesta de la solicitud http
                soup = BeautifulSoup(respuesta.text, 'html.parser')
                #print(soup)
                # Aquí puedes realizar operaciones de Web Scraping
                # # Iniciamos el bloque try para generar una excepción de forma segura
                try:
                    # Buscamos los elementos en el html que se llamen article y que tengan la clase card-news
                    noticias = soup.find_all('article', class_='card-news')
                    # Evaluamos la condición noticas
                    if noticias:
                        #print(noticias)
                        # creamos la lista vacía llamada lista_categorías
                        lista_categorias = []
                        # accedemos a las propiedades de cada artículo mediante la variable articulo tomando el valor de cada elemento de la lista noticias
                        for articulo in noticias:
                            #print(articulo)
                            # # Iniciamos el bloque try para generar una excepción de forma segura
                            try:
                                # buscamos en la categoría título para encontrar el primer elemento a en la clase oop-link y usamos text.strip para elimintar espacios en blanco al principio y final del texto
                                titulo = articulo.find('a', class_='oop-link').text.strip()
                                # buscamos en la categoría url_noticia para encontrar el primer elemento a en la calse oop-link y extraemos mediante href la url de la noticia
                                url_noticia = articulo.find('a', class_='opp-link')['href']
                                #print(url_noticia)
                                # Usamos el método split para dividir la cadena url_noticia en una lista de subcadenas usando '/' como delimitador
                                lista_url_noticia = url_noticia.split('/')
                                # intentamos acceder a la posición 1 de la lista y comparamos si dicha posición no se trata de una catena vacía
                                if lista_url_noticia[1] != '':
                                # Asignamos a la variable categoría el valor del elemento en la posición 1 de la lista_url noticias
                                    categoria = lista_url_noticia[1]
                                #Si la condición anterior es falsa:
                                else:
                                # Asignamos a la variable categoría el valor del elemento en la posición 3 de la lista_url noticias
                                    categoria = lista_url_noticia[3]
                                # Agregamos el valor de la variable categorías a la lista_categorias
                                lista_categorias.append(categoria)
                                # Dividimos la cadena url_noticia en lista de subcadenas usando '--' como delimitador intentando extraer info de la fecha de la noticia
                                lista_fecha = url_noticia.split('--')
                                # eliminamos la cadena 'html' de la segunda posición de la lista_fecha, mediante el método replace accediendo a la posición con una cadena vacía
                                fecha_caracteres = lista_fecha[1].replace('.html', '')
                                # print(fecha_caracteres)
                                # print(fecha_caracteres[0:4])
                                # print(fecha_caracteres[4:6])
                                # print(fecha_caracteres[6:8])
                                # print(fecha_caracteres[8:10])
                                # print(fecha_caracteres[10:12])
                                # print(fecha_caracteres[12:14])
                                fecha = transformar_fecha(fecha_caracteres)
                                """fecha = datetime(int(fecha_caracteres[0:4]), int(fecha_caracteres[4:6]),
                                                 int(fecha_caracteres[6:8]))"""
                                # Usamos el método strftime para formatear el objeto fecha en una cadena de texto. (y = año, m = mes, d = día)
                                fecha = fecha.strftime("%Y/%m/%d")
                                # Eliminamos comillas simples, dobles y comas de la cadena título
                                titulo = transformar_titulo(titulo)
                                #titulo = titulo.replace('\'','').replace('"','').replace(',','')
                                # Verificamos si el valor de la variable categoría_scraping es 'todas'
                                if categoria_scraping == 'todas':
                                    # # Iniciamos el bloque try para generar una excepción de forma segura
                                    try:
                                    # Abrir el archivo 'noticias.csv' en modo escritura al final (a = apppend)
                                        with open('../data/noticias.csv', 'a') as f:
                                            #Concatenamos las variables (titulo, url_noticia, categoría y fecha en formato stf, con comas entre ellas, y añadimos un carácter de nueva línea mediante '\n'
                                            f.write(titulo+','+url_noticia+','+categoria+','+str(fecha)+'\n')
                                        # Analizar el contenido con BeautifulSoup
                                    # Si en el bloque try ocurre alguna excepción se utiliza el except y:
                                    except:
                                        # Se imprime el siguiente error.
                                        print("ERROR: no se pudo anexar la noticia al archivo noticias.csv")
                                # Va con el bloque if categoría == 'todas' y se ejecuta si esto es falso
                                else:
                                    # Si la variable categoría es igual a la variable categoría_scraping
                                    if categoria == categoria_scraping:
                                        # # Iniciamos el bloque try para generar una excepción de forma segura
                                        try:
                                            # Abrir el archivo en modo escritura para anexar la noticia (a = append) al final
                                            with open('../data/noticias_'+categoria_scraping+'.csv', 'a') as f:
                                                # construimos una cadena que tiene la información de una noticia en csv (con las variables que hay dentro) separada por comas y seguida por un carácter de nueva línea ('\n')
                                                f.write(titulo + ',' + url_noticia + ',' + categoria + ',' + str(
                                                    fecha) + '\n')
                                            # Analizar el contenido con BeautifulSoup
                                        # Si no se puede hacer lo anterior:
                                        except:
                                            # imprimimos el siguiente error.....
                                            print("ERROR: no se pudo anexar la noticia al archivo noticias.csv")
                            # si no se puede hacer (excepto):
                            except:
                                # Intentamos
                                try:
                                    # Intentamos extraer el título de noticias del html buscando el primer elemento 'a' con la clase 'lnk'. Con 'strip' eliminamos los espacios en blanco al inicio o final del título
                                    titulo = articulo.find('a', class_='lnk').text.strip()
                                    # Extraemos la url de noticias del html buscando el primer elemento 'a' con la clase 'lnk' y extraemos su atributo 'href' que contiene la url del artículo vinculado
                                    url_noticia = articulo.find('a', class_='lnk')['href']
                                    # Dividimos la url_noticas en una lista de componentes con '/'. 'lista_url_noticias tendrá distintos segmentos que buscamos.
                                    lista_url_noticia = url_noticia.split('/')
                                    # Comprobamos si el elemento situado en la posición [1] de la lista es una cadena vacía
                                    if lista_url_noticia[1] != '':
                                        # Si es cadena vacía le asignamos el elemento situado en la posicion [1] de la lista
                                        categoria = lista_url_noticia[1]
                                        # Si no
                                    else:
                                        # Le asignamos el elemento situado en la posición [3] de la lista
                                        categoria = lista_url_noticia[3]
                                    # Agregamos al final de la lista la categoría del artículo
                                    lista_categorias.append(categoria)
                                    # Dividimos la url_noticias en una lista de componentes con '--'. La lista resultante tendrá 2 elementos, primero el protocolo y el dominio web y segundo la fecha del artículo de noticias
                                    lista_fecha = url_noticia.split('--')
                                    # Extraemos lista_fecha. Si se encuentra en la posición [1] e incluye la extensión 'html',eliminamos la extensión de la cadena
                                    fecha_caracteres = lista_fecha[1].replace('.html', '')
                                    #print(fecha_caracteres)
                                    #print(fecha_caracteres[0:4])
                                    #print(fecha_caracteres[4:6])
                                    #print(fecha_caracteres[6:8])
                                    #print(fecha_caracteres[8:10])
                                    #print(fecha_caracteres[10:12])
                                    #print(fecha_caracteres[12:14])
                                    # Convertimos fecha de una cadena de caracteres a un objeto datetime.La cadena tiene la fecha en formato YYYYMMDD
                                    fecha = datetime(int(fecha_caracteres[0:4]), int(fecha_caracteres[4:6]), int(fecha_caracteres[6:8]))
                                    # Convertimos la fecha a un formato legible ("%Y/%m/%d" = AAAA/MM/DD)
                                    fecha = fecha.strftime("%Y/%m/%d")
                                    # Eliminamos ', " y , de título con replace "
                                    titulo = titulo.replace('\'', '').replace('"', '').replace(',', '')
                                    # Comprobamos si la variable 'categoria_scrapping' tiene el valor 'todas'.
                                    if categoria_scraping == 'todas':
                                        # Iniciamos el bloque try para genera una excepción de forma segura
                                        try:
                                           # Abrimos el archivo 'noticias.csv' en modo escritura
                                            with open('../data/noticias.csv', 'a') as f:
                                                # Escribimos los datos (título, url, categoría y fecha) separados con una compa y con salto de línea
                                                f.write(titulo + ',' + url_noticia + ',' + categoria + ',' + str(
                                                    fecha) + '\n')
                                            # Analizar el contenido con BeautifulSoup
                                           #excepto
                                        except:
                                            # si no se puede realizar lo anterior, se imprimirá en consola el siguiente error
                                            print("ERROR: no se pudo anexar la noticia al archivo noticias.csv")
                                    # Si no
                                    else:
                                        # si categoría es igual a categoría_scrapping
                                        if categoria == categoria_scraping:
                                            # Iniciamos el bloque try para genera una excepción de forma segura
                                            try:
                                                #abrimos un archivo nuevo csv que se llama noticias + categoria_scraping en modo 'a' para añadir nuevos datos.
                                                with open('../data/noticias_' + categoria_scraping + '.csv', 'a') as f:
                                                    # Escribimos los datos (título, url_noticia, categoría y fecha), separados por una coma y con un salto de línea al final.
                                                    f.write(titulo + ',' + url_noticia + ',' + categoria + ',' + str(
                                                        fecha) + '\n')
                                                # Analizar el contenido con BeautifulSoup
                                            # Si no se puede hacer lo anterior(excepto)
                                            except:
                                                # Imprimimos el siguiente error.....
                                                print("ERROR: no se pudo anexar la noticia al archivo noticias.csv")
                                # Si no se puede hacer lo anterior:
                                except:
                                    # No realizamos nada y pasamos
                                    pass
                        #print(lista_categorias)
                        # Creamos un conjunto a partir de lista_categorias para tener solo elementos únicos y no duplicados, sin orden específico.
                        conjunto_categorias = set(lista_categorias)
                        #print(conjunto_categorias)
                    # Si la condición if noticas es falso ejecutamos el else:
                    else:
                        # imprimimos el siguiente eror
                        print(f"Error La pagina {url} no contiene noticias")
                # Si no podemos encontrar la palabra article en la clase card-news, ejecutamos la siguiente excepción
                except:
                    # imprimimos en pantalla el siguiente error....
                        print(f"ERROR: No se pudo encontrar articulos en el codigo html")
            # si no conseguimos convertir la página a html después de la solicitud, ejecutamos la siguiente excepción:
            except:
                # imprimimos en pantalla el siguiente error.....
                print(f"ERROR: no se pudo convertir la pagina a codigo html")
        # En caso de que la respuesta no sea 200
        else:
            # imprimos el siguiente error.
            print(f"Error al obtener la página web. Código de estado: {respuesta.status_code}")
    # Si una vez generada la solicitud no se puede abrir la página o hay cualquier error generamos la siguiente excepción:
    except:
        # imprimimos en pantalla el siguiente error
        print(f"ERROR: No se puede abrir la web pagina {url} o existe un error al procesarla")
    # Devolvemos conjunto_categorías como valor de la función webscraping
    return conjunto_categorias

# llamamos a la función webscraping para obtener la lista de categorías de noticias de la web de Telemadrid
listado_categorias = webscraping('https://www.telemadrid.es/','todas')
# Iniciamos la variable selección para almacenar la opción que seleccione el usuario con el valor x
seleccion = 'x'
# Iniciamos el bucle while hasta que selección tenga el valor '0'
while seleccion != '0':
    # Imprimimos el encabezado de la lista de categorías
    print("Lista de categorias: ")
    # Usamos la variable i para almacenar el número de la categoría actual y le asignamos el valor '1'
    i = 1
    # Comenzamos con el bucle for para recorrer la lista de categorías
    for opcion in listado_categorias:
        # Imprimios el número de la categoría actual y el nombre
        print(f"{i}.- {opcion}")
        # Incrementamos el valor de 'i' en '1' para que el número de la categoría sea el siguiente en la secuencia
        i = i + 1
    # En caso de querer salir, pulsamos el número '0'
    print("0.- Salir")
    # Solicitamos al usuario que seleccione una opción mediante un número
    seleccion = input("Por favor seleccione una opcion indicando un numero:")
    # Convertimos en una lista el listado de categorías para acceder mediante un índice
    categorias_listas = list(listado_categorias)
    # Usamos el indice int(seleccion)-1 para obtener la categoría que selecciona el usuario
    categoria_seleccionada = categorias_listas[int(seleccion)-1]
    # Llamamos a la función webscraping para procesar la categoría que ha seleccionado el usuario
    webscraping('https://www.telemadrid.es/', categoria_seleccionada)
