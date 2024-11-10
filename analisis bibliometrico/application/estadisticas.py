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
from prettytable import PrettyTable
import tkinter as tk
import networkx as nx
import matplotlib.pyplot as plt


class Estadisticas():

    #VARIABLES GLOBALES
    data = None #contiene los datos ordenados


    #metodo constructor
    def __init__(self):
        
        self.cargarDatos()
        self.estandarizarTiposDatos()


    #Genera una grafica que muestra los autores
    def mostrarGraficaDatosParciales(self,counting_data:dict,mensaje_titulo:str,cantidad_datos_mostrar:int):
        """
            Mostrar una grafica de barras con el numero de datos elejido, este numero de datos seran extraidos de mayor 
            a menor

            parametros
                couting_autores - diccionario de datos a imprimir
                mensaje - mensaje titulo que aparece en la grafica
                cantidad_datos - es la cantidad de datos que seran impresos
        """

        # Filtrar autores con más de 5 ocurrencias
        top_data = sorted(counting_data.items(), key=lambda x:x[1] , reverse=True)[:cantidad_datos_mostrar]


        #se extraen los datos para la grafica
        keys = [keys for keys,_ in top_data ]
        values = [values for _,values in top_data]

        plt.bar(keys,values)


        # Añadir etiquetas
        plt.xlabel('Datos')
        plt.ylabel('Cantidad')
        plt.title(mensaje_titulo)

        # Mostrar el gráfico
        plt.xticks(rotation=90)  # Rotar etiquetas si son largas
        plt.show()



    #metodo que genera una grafica para todos los datos recibidos
    def mostrarGraficaDatosCompletos(self,product_type_couting:dict,mensaje:str):
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
    def cargarDatos(self):

        """
            Se lee el archivo csv con la data y se almacena en una variable
        """
        

        #extraer direccion del archivo
        base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        file_path = os.path.join(base_dir, 'data', 'dataOrd.csv')

        #leer el archivo
        self.data = pd.read_csv(file_path, nrows=10150, encoding='utf-8',
                        on_bad_lines='skip',
                        encoding_errors='replace')



    #estandariza el tipo de dato de cada columna 
    def estandarizarTiposDatos(self):
        """
            Para evitar errores en la lectura de los datos y confundir tipos, se estandarizan los 
            tipos de datos desde el inicio
        """
        #se genera una columna que contiene el primer autor
        self.data['FirstAuthor']=self.data['Authors'].apply(lambda x: x.split(';')[0].strip().split(',')[0])

        #se estandariza el tipo de dato de cada columna
        self.data['Authors'] = self.data['Authors'].astype(str)
        self.data['Year'] = self.data['Year'].astype(int).fillna(0)
        self.data['Affiliations']=self.data['Affiliations'].astype(str)
        self.data['Source title']=self.data['Source title'].astype(str)
        self.data['Publisher']=self.data['Publisher'].astype(str)
        self.data['Title']=self.data['Title'].astype(str)
        self.data['Source']=self.data['Source'].astype(str)



    #filta la base de datos con respecto a un año especifico
    def filtrar_year_data(self,year:int):
        """
        Filtra la base de datos para un año específico, permitiendo analizar y procesar datos de ese año.

        Parámetros:
            year (int): Año para filtrar los datos. Si se ingresa 0, se devuelve toda la data sin filtrar.

        Retorna:
            DataFrame: Datos filtrados por el año especificado o toda la data si `year` es 0.
        """

        #si entra un 0 el usuario no especifico año
        if year == 0:
            return self.data
        
        return self.data[self.data['Year'] == year]



    #hacer conteno de autores
    def analizarAutores(self,year):

        """
            Se extrae el primer autor de cada producto y se hace un contedo de las veces 
            que aparece cada autor

        """
        filter_data = self.filtrar_year_data(year)

        #extraer el primer autor    
        autores = filter_data['FirstAuthor']

        counting_autores={}

        #hacer un conteo de los autores
        for autor in autores:
            if autor != 'Null':
                if autor in counting_autores:
                    counting_autores[autor]+=1
                else:
                    counting_autores[autor]=1

        self.mostrarGraficaDatosParciales(counting_autores,f'Grafica de los 15 mejores autores en el año {year}',15)



    #hacer un conteo de los años de la publicacion de cada articulo
    def analizarFecha(self):
        """
            realizar un conteo de los años de publicacion de cada articulo
        """

        years_couting={} #diccionario de años

        #conteo de años
        for year in self.data['Year']:
            if year != 0:
                if year in years_couting:
                    years_couting[year]+=1
                else:
                    years_couting[year]=1

        self.mostrarGraficaDatosCompletos(years_couting,'Grafica de años')



    #metodo que cuenta la cantidad de cada tipo de producto
    def analizarTipoProducto(self,year:int):

        """
            Contar la cantidad de veces que aparece cada tipo de producto
            los tipos de producto que hay son
            *articulo
            *libro
            *conferencia

            despues de realizar el conteo, se imprime una grafica con el resultado de los datos
        """
        #data filtrada
        filter_data = self.filtrar_year_data(year)

        product_type_couting={} #diccionario de tipos de productos

        for item in filter_data['ProductType']:
            if item and item in product_type_couting:
                product_type_couting[item]+=1
            else:
                product_type_couting[item]=1

        self.mostrarGraficaDatosCompletos(product_type_couting,'Grafica de tipos de producto')



    #contar las instituciones de todos los datos
    def analizarInstituciones(self,year:int):


        """
            Se cuentan las instituciones que aparecen en la columna afiliattions
            y se imprimen las 5 primeras instituciones
        """
        filter_data =self.filtrar_year_data(year)

        instituciones={}

        #se recorren las afiliaciones
        for afiliacion in filter_data['Affiliations']:

            if afiliacion != 'Null':
                institucion = str(afiliacion).split(',')[0]#se extrae la instituciones
                if  institucion in instituciones:
                    instituciones[institucion]+=1
                else:
                    instituciones[institucion]=1


        self.mostrarGraficaDatosParciales(instituciones,'Grafica de instituciones',10)



    #contar todos los journal que han publicado 
    def analizarJournal(self,year:int):
        """
            Realizar un conteo de todos los journal mas representativos e imprimir los 
            mejores journal
        """
        filter_data=self.filtrar_year_data(year)

        journal_couting={}

        for item in filter_data['Source title']:
            if item != 'Null':
                if item in journal_couting:
                    journal_couting[item]+=1
                else:
                    journal_couting[item]=1

        self.mostrarGraficaDatosParciales(journal_couting,'3 mejores journal',3)



    #contar todos los publisher presentes
    def analizarPublisher(self,year:int):
        """
            Contar todos los publisher de cada producto, y mostrar los publisher top que aparecen por cada articulo
        """
        filter_data = self.filtrar_year_data(year)

        publisher_couting = {}

        for item in filter_data['Publisher']:
            if item != 'Null':
                if  item in publisher_couting:
                    publisher_couting[item]+=1
                else:
                    publisher_couting[item]=1

        self.mostrarGraficaDatosParciales(publisher_couting,'grafica de los 5 mejores publisher',5)



    #contar la cantidad de productos por cada base de daatos
    def analizarBaseDatos(self,year:int):
        """
            Hacer un conteo de las bases de datos y mostrar en una grafica de barras todas las bases
            y la cantidad de articulos de cada uno
        """
        filter_data=self.filtrar_year_data(year)

        data_bases_couting={}

        for item in filter_data['Source']:
            if item != 'Null':
                if item and item in data_bases_couting:
                    data_bases_couting[item]+=1
                else:
                    data_bases_couting[item]=1

        self.mostrarGraficaDatosCompletos(data_bases_couting,'Cantidad de bases de datos')



    #impritmir los articulos mas citados
    def analizarArticuloMasCitado(self,year:int):
        """
        Se extraen los artículos y sus citaciones y se imprimen los 15 artículos más citados
        """
        filter_data = self.filtrar_year_data(year)

        citaciones_por_articulo = {}

        for _, row in filter_data.iterrows():  # `_` omite el índice, y `row` es la Serie de la fila
            if row['Title'] != 'Null' and row['Cited by'] != 0:  # Verifica que ambos valores existan
                citaciones_por_articulo[row['Title']] = int(row['Cited by'])

        self.mostrarGraficaDatosParciales(citaciones_por_articulo, 'artículos más citados', 5)
        


    #analizar los mejores autores y su aparicion en cada base de datos
    def analizar_database_autor(self):
        """
        Realizar un analisis de los mejores autores generales y cuantas veces aparecen en cada base de datos,
        se mostrara una tabla con los resultados
        """
        # Filtrar autores donde 'FirstAuthor' no sea 'Null'
        data_filtrada = self.data[self.data['FirstAuthor'] != 'Null']

        # Agrupa los datos por 'Autor' y 'Base de datos', y cuenta las ocurrencias
        resultados = data_filtrada.groupby(['FirstAuthor', 'Source']).size().unstack(fill_value=0)

        # Agrega una columna de total de apariciones para ordenar
        resultados['Total'] = resultados.sum(axis=1)

        # Ordena por el total de apariciones y selecciona los 15 mejores
        mejores_15 = resultados.sort_values(by='Total', ascending=False).head(15)

        # Elimina la columna 'Total' de la visualización final si solo quieres ver el desglose por base de datos
        mejores_15 = mejores_15.drop(columns='Total')

        # Muestra la tabla
        print("Conteo de apariciones de los 15 mejores autores en cada Base de Datos:")
        print(mejores_15)


        tabla = PrettyTable()
        tabla.field_names = ["Authors"] + list(mejores_15.columns)
        for index, row in mejores_15.iterrows():
            
            tabla.add_row([index] + list(row))
        

            # Crear la ventana de Tkinter
        root = tk.Tk()
        root.title("Tabla de Datos de los 15 Mejores Autores")

        # Crear y mostrar el texto con el contenido de la tabla en la interfaz
        text = tk.Text(root, wrap="none")
        text.insert(tk.END, tabla.get_string())
        text.config(state="disabled")  # Hacer que el texto sea de solo lectura
        text.pack()

        # Ejecutar la interfaz
        root.mainloop()



    def analizar_journal_articulo(self):
        """
        Realizar un conteo de los articulos que contiene cada journal
        y se imprimen los 3 mas relevantes

        """

        journal_couting={}

        for _,item in self.data.iterrows():
            if item['Source title'] != 'Null': #and item['Product type']=='article':
                if item['Source title'] in journal_couting:
                    journal_couting[item['Source title']]+=1
                else:
                    journal_couting[item['Source title']]=1

        self.mostrarGraficaDatosParciales(journal_couting,'3 mejores journal',3)


    #hacer un analisis de los mejores autores por cada journal
    def analizar_autores_journal(self,cantidadJournal:int):  
        """
        identificar el  autor con mas publicaciones de los n mejores jorunal y se 
        imprimen los resultados
        """

        listaJournal:dict = self.obtener_mejores_journal(cantidadJournal)#obtener los 3 mejores journal

        for _,item in self.data.iterrows(): #se recorre el dataframe

            journal = item['Source title']#se extrae el journal
            autor = item['FirstAuthor']

            if journal in listaJournal:
                listaJournal=self.agregar_autor_journal(journal,autor,listaJournal)

        self.imprimir_autores_journal(listaJournal)




    #imprimir el mejor autor de cada jorunal
    def imprimir_autores_journal(self,listaJournal:dict):
        
        for journal,authors in listaJournal.items():
            mejor_autor=self.extraer_mejor_autor(authors)

            print(f'El mejor autor del journal {journal} es el autor {mejor_autor}')



    #extraer el item con mas ocurrencias de un diccionario
    def extraer_mejor_autor(self,autores:dict):

        # Ordenar los datos de mayor a menor y extraer el mejor
        top_autor = sorted(autores.items(), key=lambda x: x[1], reverse=True)[0]

        return top_autor


    #obtener los n journal que han publicado mas productos
    def obtener_mejores_journal(self,cantidad: int):
        """
        Realizar el conteo de la cantidad de productos de cada journal y seleccionar los 
        n mejores journal de la lista.

        parametros:
            cantidad - contiene la cantidad de journal que se desean obtener.
        """

        journal_couting = {}

        for _, item in self.data.iterrows():
            if item['Source title'] != 'Null':  # and item['Product type'] == 'article':
                if item['Source title'] in journal_couting:
                    journal_couting[item['Source title']] += 1
                else:
                    journal_couting[item['Source title']] = 1

        # Filtrar journals con más ocurrencias y seleccionar los top "cantidad"
        top_data = sorted(journal_couting.items(), key=lambda x: x[1], reverse=True)[:cantidad]

        # Inicializar diccionario con las llaves generadas y valores en 0
        result = {key: {} for key,_ in top_data}

        return result



    #se agrega el conteo de un autor a cada journal
    def agregar_autor_journal(self,journal:str,autor:str,listaJournal:dict):
        """
        identificar cual es el journal del producto, y cuando se identifica el journal, se agrega 
        un autor para llevar un conteo sobre el, cada autor en cada journal tendra un conteo especifico

        Parametros
            Journal - nombre del journal
            autor - nombre del autor
            listaJournal - diccionario donde se lleva el conteo de cada autor en cada journal
        """
        if autor in listaJournal[journal]:
            listaJournal[journal][autor]+=1
        else:
            listaJournal[journal][autor]=1
        
        return listaJournal



    #analizar la relacion entre el journal, articulo y pais
    def analizar_journal_articulo_pais(self,cantidad_journal,cantidad_articulos):
        """
            Analizar las 3 variables (journal, articulo,pais) con el fin de mostrar la relacion entre los mejores journal
            con los articulos mas citados, y a su vez, la relacion del articulo con sus paises de procedencia.
        """
        #1.generar un dataframe 
        #2.extraer los 10 mejores journal
        #3.almacenar los journal
        #4.extraer los 15 mejores articulos
        #5.almacenar los 15 
        #6.relacionar cada journal a los articulos
        #7.extraer el pais de cada articulo, eliminar los repetidos, y unificar
        #8.generar grafo


        #obtener los mejores journal
        journals=list(self.obtener_mejores_journal(cantidad_journal).keys())   

        #extraer los articulos mas citados en orden desendente
        articulos_mas_citados = self.data.sort_values(by='Cited by', ascending=False)[:cantidad_articulos]

        self.generar_grafo(journals,articulos_mas_citados)


    def generar_grafo(self,journals: list, articulos_mas_citados: pd.DataFrame):
        """
        Generate a graph that relates journals, articles, and publication years based on the collected data.
        """

        # Create the graph
        grafo = nx.Graph()

        # Add nodes for journals, articles, and years, along with their types
        for journal in journals:
            grafo.add_node(journal, tipo='journal')

        for _, articulo in articulos_mas_citados.iterrows():
            # Add article node
            grafo.add_node(articulo['Title'], tipo='article')

            # Add year node
            grafo.add_node(articulo['Year'], tipo='year')

            # Add edges between source journal and article
            if articulo['Source title'] in journals:
                grafo.add_edge(articulo['Source title'], articulo['Title'])

            # Add edges between article and its publication year
            grafo.add_edge(articulo['Title'], articulo['Year'])

        # Set colors based on node type
        node_colors = []
        for node in grafo.nodes(data=True):
            tipo = node[1]['tipo']
            if tipo == 'journal':
                node_colors.append('orange')
            elif tipo == 'article':
                node_colors.append('lightblue')
            elif tipo == 'year':
                node_colors.append('lightgreen')

        # Draw the graph
        pos = nx.spring_layout(grafo, k=0.5, seed=42)  # Define layout for readability
        nx.draw(grafo, pos, with_labels=True, node_color=node_colors, node_size=500, font_size=5, font_weight="bold")
        plt.show()



    #analizar la cantidad de productos de cada tipo (articulo, conferencia, libro)
    def contar_tipos_producto(self):
        """
            Contar la totalidad de los 3 tipos de productos buscados
        """
        product_type_couting = {}

        for item in self.data['Tipo']:
            if item != 'Null':
                if  item in product_type_couting:
                    product_type_couting[item]+=1
                else:
                    product_type_couting[item]=1

        self.mostrarGraficaDatosCompletos(product_type_couting,'grafica de la cantidad de productos')
