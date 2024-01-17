# importar el modulo request para extrar una pagina web
import requests
# importar el modulo bs4 la libreria BeautifulSoup para transformar el código en html
from bs4 import BeautifulSoup
# importar módulo datetime para trabajar con fechas y horas
from datetime import datetime

def transformar_fecha(fecha_caracteres):
    fecha = datetime(int(fecha_caracteres[0:4]), int(fecha_caracteres[4:6]),
                     int(fecha_caracteres[6:8]))
    return fecha

def transformar_titulo(titulo):
    titulo = titulo.replace('\'', '').replace('"', '').replace(',', '')
    return titulo


def webscraping(url_scraping,categoria_scraping='todas'):
    # URL de telemadrid
    url = url_scraping

    # Realizar la petición
    try:
        #Realizamos la solicitud http get a la url que hemos especificado en la biblioteca requests
        respuesta = requests.get(url)
        #print(respuesta)
        #print(respuesta.text)
        # Verificar si la petición fue exitosa (código 200)
        if respuesta.status_code == 200:
            # probramos con la siguiente excepción
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
            # probamos la siguiente excepción
            try:
                # usamos BeautifulSoup para analizar el contenido HTML de la respuesta de la solicitud http
                soup = BeautifulSoup(respuesta.text, 'html.parser')
                #print(soup)
                # Aquí puedes realizar operaciones de Web Scraping
                # ...
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
                            # probamos la siguiente excepción
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
                                    # Intentamos:
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
                                        # Intentamos
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
                                    # Usamos BeautifoulSoup para buscar el elemento 'a' en la clase 'lnk' en la variable articulo y extraemos el texto mediante strip()
                                    titulo = articulo.find('a', class_='lnk').text.strip()
                                    url_noticia = articulo.find('a', class_='lnk')['href']
                                    lista_url_noticia = url_noticia.split('/')
                                    if lista_url_noticia[1] != '':
                                        categoria = lista_url_noticia[1]
                                    else:
                                        categoria = lista_url_noticia[3]
                                    lista_categorias.append(categoria)
                                    lista_fecha = url_noticia.split('--')
                                    fecha_caracteres = lista_fecha[1].replace('.html', '')
                                    #print(fecha_caracteres)
                                    #print(fecha_caracteres[0:4])
                                    #print(fecha_caracteres[4:6])
                                    #print(fecha_caracteres[6:8])
                                    #print(fecha_caracteres[8:10])
                                    #print(fecha_caracteres[10:12])
                                    #print(fecha_caracteres[12:14])
                                    fecha = datetime(int(fecha_caracteres[0:4]), int(fecha_caracteres[4:6]), int(fecha_caracteres[6:8]))
                                    fecha = fecha.strftime("%Y/%m/%d")
                                    titulo = titulo.replace('\'', '').replace('"', '').replace(',', '')
                                    if categoria_scraping == 'todas':
                                        try:
                                            with open('../data/noticias.csv', 'a') as f:
                                                f.write(titulo + ',' + url_noticia + ',' + categoria + ',' + str(
                                                    fecha) + '\n')
                                            # Analizar el contenido con BeautifulSoup
                                        except:
                                            print("ERROR: no se pudo anexar la noticia al archivo noticias.csv")
                                    else:
                                        if categoria == categoria_scraping:
                                            try:
                                                with open('../data/noticias_' + categoria_scraping + '.csv', 'a') as f:
                                                    f.write(titulo + ',' + url_noticia + ',' + categoria + ',' + str(
                                                        fecha) + '\n')
                                                # Analizar el contenido con BeautifulSoup
                                            except:
                                                print("ERROR: no se pudo anexar la noticia al archivo noticias.csv")
                                except:
                                    pass
                        #print(lista_categorias)
                        conjunto_categorias = set(lista_categorias)
                        #print(conjunto_categorias)
                    else:
                        print(f"Error La pagina {url} no contiene noticias")
                except:
                        print(f"ERROR: No se pudo encontrar articulos en el codigo html")
            except:
                print(f"ERROR: no se pudo convertir la pagina a codigo html")
        else:
            print(f"Error al obtener la página web. Código de estado: {respuesta.status_code}")
    except:
        print(f"ERROR: No se puede abrir la web pagina {url} o existe un error al procesarla")
    return conjunto_categorias


listado_categorias = webscraping('https://www.telemadrid.es/','todas')
seleccion = 'x'
while seleccion != '0':
    print("Lista de categorias: ")
    i = 1
    for opcion in listado_categorias:
        print(f"{i}.- {opcion}")
        i = i + 1
    print("0.- Salir")
    seleccion = input("Por favor seleccione una opcion indicando un numero:")
    categorias_listas = list(listado_categorias)
    categoria_seleccionada = categorias_listas[int(seleccion)-1]
    webscraping('https://www.telemadrid.es/', categoria_seleccionada)
