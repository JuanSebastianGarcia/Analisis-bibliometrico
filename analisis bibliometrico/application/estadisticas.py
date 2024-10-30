"""
Lista de las variables que hay que procesar 

    Primer autor del producto
    Año de publicación
    Tipo de producto (artículos, conferencias, capítulos de libro)
    Afiliación del primer autor
    Journal
    Publisher
    Base de datos
    Cantidad de citaciones por artículo

    cada variable tendra su forma de ser procesada
"""
#IMPORTS
import os
import pandas as pd
import matplotlib.pyplot as plt


#VARIABLES GLOBALES
data = None #contiene los datos ordenados


#Genera una grafica que muestra los autores
def mostrarGraficaDatosParciales(counting_autores:dict,mensaje:str,cantidad_datos:int):
    """
        Mostrar una grafica de barras con el numero de datos elejido, este numero de datos seran extraidos de mayor 
        a menor

        parametros
            couting_autores - diccionario de datos a imprimir
            mensaje - mensaje titulo que aparece en la grafica
            cantidad_datos - es la cantidad de datos que seran impresos
    """
    # Filtrar autores con más de 5 ocurrencias
    top_autores = sorted(counting_autores.items(), key=lambda x:x[1] , reverse=True)[:cantidad_datos]


    #se extraen los datos para la grafica
    keys = [autor for autor,_ in top_autores ]
    values = [conteo for _,conteo in top_autores]

    plt.bar(keys,values)

    # Añadir etiquetas
    plt.xlabel('Datos')
    plt.ylabel('Cantidad')
    plt.title(mensaje)

    # Mostrar el gráfico
    plt.xticks(rotation=90)  # Rotar etiquetas si son largas
    plt.show()



#metodo que genera una grafica para todos los datos recibidos
def mostrarGraficaDatosCompletos(product_type_couting:dict,mensaje:str):
    """
        Generar una grafica a partir de un diccionario de datos 

        paramentros:
            product_type_couting - diciconario que contiene los datos a imprimir
            mensaje - mensaje para el titulo de la grafica
    """

    #extraccion de datos
    values = list(product_type_couting.values())
    keys = list(product_type_couting.keys())

    plt.bar(keys,values)

    # Añadir etiquetas
    plt.xlabel('Datos')
    plt.ylabel('Cantidad')
    plt.title(mensaje)

    # Mostrar el gráfico
    plt.xticks(rotation=90)  # Rotar etiquetas si son largas
    plt.show()



#carga lso datos del csv a la variable data
def cargarDatos():

    """
        Se lee el archivo csv con la data y se almacena en una variable
    """
    global data

    #extraer direccion del archivo
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    file_path = os.path.join(base_dir, 'data', 'dataOrd.csv')

    #leer el archivo
    data = pd.read_csv(file_path, nrows=10150, encoding='utf-8',
                       on_bad_lines='skip',
                       encoding_errors='replace')



#estandariza el tipo de dato de cada columna 
def estandarizarTiposDatos():
    """
        Para evitar errores en la lectura de los datos y confundir tipos, se estandarizan los 
        tipos de datos desde el inicio
    """
    global data

    data['Authors'] = data['Authors'].astype(str)
    data['Year'] = data['year'].astype(int).fillna(0)
    data['Affiliations']=data['Affiliations'].astype(str)
    data['Source title']=data['Source title'].astype(str)
    data['Publisher']=data['Publisher'].astype(str)



#hacer conteno de autores
def analizarAutores():

    """
        Se extrae el primer autor de cada producto y se hace un contedo de las veces 
        que aparece cada autor

    """
    global data

    #extraer el primer autor    
    autores = data['Authors'].apply(lambda x: x.split(';')[0].strip().split(',')[0])

    counting_autores={}

    #hacer un conteo de los autores
    for autor in autores:
        if autor != 'null':
            if autor in counting_autores:
                counting_autores[autor]+=1
            else:
                counting_autores[autor]=1

    mostrarGraficaDatosParciales(counting_autores,'Grafica de los 15 mejores autores',15)



#hacer un conteo de los años de la publicacion de cada articulo
def analizarFecha():
    """
        realizar un conteo de los años de publicacion de cada articulo
    """

    global data #variable de datos

    years_couting={} #diccionario de años

    #conteo de años
    for year in data['Year']:
        if year is not 0:
            if year in years_couting:
                years_couting[year]+=1
            else:
                years_couting[year]=1

    mostrarGraficaDatosCompletos(years_couting,'Grafica de años')



#metodo que cuenta la cantidad de cada tipo de producto
def analizarTipoProducto():

    """
        Contar la cantidad de veces que aparece cada tipo de producto
        los tipos de producto que hay son
        *articulo
        *libro
        *conferencia

        despues de realizar el conteo, se imprime una grafica con el resultado de los datos
    """
    global data #dataframe de datos
    product_type_couting={} #diccionario de tipos de productos

    for item in data['ProductType']:
        if item and item in product_type_couting:
            product_type_couting[item]+=1
        else:
            product_type_couting[item]=1

    mostrarDatosCompletos(product_type_couting,'Grafica de tipos de producto')




#contar las instituciones de todos los datos
def analizarInstituciones():


    """
        Se cuentan las instituciones que aparecen en la columna afiliattions
        y se imprimen las 5 primeras instituciones
    """

    global data #dataframe de datos

    instituciones={}

    #se recorren las afiliaciones
    for afiliacion in data['Affiliations']:

        if afiliacion is not 'null':
            institucion = str(afiliacion).split(',')[0]#se extrae la instituciones
            if  institucion in instituciones:
                instituciones[institucion]+=1
            else:
                instituciones[institucion]=1


    mostrarGraficaDatosParciales(instituciones,'Grafica de instituciones',10)



#contar todos los journal que han publicado 
def analizarJournal():
    """
        Realizar un conteo de todos los journal mas representativos e imprimir los 
        mejores journal
    """
    global data #dataframe de datos

    journal_couting={}

    for item in data['Source title']:
        if item and item in journal_couting:
            journal_couting[item]+=1
        else:
            journal_couting[item]=1

    mostrarGraficaDatosParciales(journal_couting,'3 mejores journal',3)



#contar todos los publisher presentes
def analizarPublisher():
    """
        Contar todos los publisher de cada producto, y mostrar los publisher top que aparecen por cada articulo
    """
    global data #dataframe de datos

    publisher_couting = {}

    for item in data['Publisher']:
        if item and item in publisher_couting:
            publisher_couting[item]+=1
        else:
            publisher_couting[item]=1

    mostrarGraficaDatosCompletos(publisher_couting,'grafica de publisher')



#contar la cantidad de productos por cada base de daatos
def analizarBaseDatos():
    """
        Hacer un conteo de las bases de datos y mostrar en una grafica de barras todas las bases
        y la cantidad de articulos de cada uno
    """
    global data # dataframe de datos

    data_bases_couting={}

    for item in data['Source']:
        if item and item in data_bases_couting:
            data_bases_couting[item]+=1
        else:
            data_bases_couting[item]=1

    mostrarGraficaDatosCompletos(data_bases_couting,'Cantidad de bases de datos')



#impritmir los articulos mas citados
def analizarArticuloMasCitado():
    """
    Se extraen los artículos y sus citaciones y se imprimen los 15 artículos más citados
    """
    global data

    citaciones_por_articulo = {}

    for _, row in data.iterrows():  # `_` omite el índice, y `row` es la Serie de la fila
        if row['Title'] and row['Cited by']:  # Verifica que ambos valores existan
            citaciones_por_articulo[row['Title']] = int(row['Cited by'])

    mostrarGraficaDatosParciales(citaciones_por_articulo, 'artículos más citados', 5)
    



#https://go.microsoft.com/fwlink/?LinkID=533483#vscode

if __name__ =='__main__':

    #preparacion
    cargarDatos()
    estandarizarTiposDatos()

    #hacer una analisis de las instituciones
    #analizarAutores()

    #hacer un analisis de los años de publicacion
    #analizarFecha()


    #hacer un analisis de los tipos de producto
    #contarTiposProducto()


    #hacer un analizis de las instituciones
    #analizarInstituciones()

    #hacer un analisis del journal de cada producto
    #analizarJournal()

    #hacer un analisis del publisher
    #analizarPublisher()

    #hacer un analisis de la base de datos
    #analizarBaseDatos()

    analizarArticuloMasCitado()