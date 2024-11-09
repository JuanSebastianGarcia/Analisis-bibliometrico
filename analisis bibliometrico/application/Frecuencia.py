import os
import pandas as pd
import ast
import re
from sklearn.feature_extraction.text import CountVectorizer
from wordcloud import WordCloud
import matplotlib.pyplot as plt

class Frecuencia:

    # Método constructor
    def __init__(self):
        self.cargar_data()
        self.sinonimos_dict = {}  # Diccionario de sinónimos inicializado
        self.crear_diccionario_sinonimos()



    # Cargar el archivo de palabras especiales y el de la data
    def cargar_data(self):
        """
        Cargar los archivos con los que se va a trabajar: el archivo con
        las bases de datos bibliográficas, además de las palabras especiales
        que van a ser procesadas.
        """
        # Cargar base de datos bibliográfica
        base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

        file_path_data = os.path.join(base_dir, 'data', 'dataOrd.csv')
        self.data = pd.read_csv(file_path_data, nrows=8509, encoding='utf-8',
                                on_bad_lines='skip', encoding_errors='replace')
        
        # Cargar palabras especiales
        file_path_palabras = os.path.join(base_dir, 'data', 'Palabras_especiales.csv')
        self.palabras_especiales = pd.read_csv(file_path_palabras, nrows=137, encoding='utf-8',
                                               on_bad_lines='skip', encoding_errors='replace')



    # Crear el diccionario de sinónimos
    def crear_diccionario_sinonimos(self):
        """
        Crear un diccionario donde cada sinónimo apunta a su palabra principal
        para facilitar el reemplazo en los textos.
        """
        for _, row in self.palabras_especiales.iterrows():
            palabra_principal = str(row['Palabra']).lower()
            # Convertir la columna de sinónimos a lista si no está vacía
            if row['Sinonimos'] != '[]':
                sin_list = ast.literal_eval(row['Sinonimos'])
                for sinonimo in sin_list:
                    self.sinonimos_dict[str(sinonimo).lower()] = palabra_principal
        
        # Ordenar el diccionario para que reemplace primero las frases más largas
        self.sinonimos_dict = dict(sorted(self.sinonimos_dict.items(), key=lambda x: len(x[0]), reverse=True))



    # Reemplazar sinónimos en un texto
    def reemplazar_sinonimos(self, texto):
        """
        Reemplaza todos los sinónimos en el texto dado según el diccionario de sinónimos.
        """
        # Crear un patrón que capture todos los sinónimos como palabras o frases completas
        patron = re.compile(r'\b(' + '|'.join(re.escape(sinonimo) for sinonimo in self.sinonimos_dict.keys()) + r')\b')


        # Reemplazar sinónimos utilizando el diccionario
        return patron.sub(lambda match: self.sinonimos_dict[match.group(0)], texto)


    #unificar los sinonimos en una sola palabra
    def unificar_sinonimos(self):
        """
        Se hace el remplazo de los sinonimos de cada palabra, por su palabra original
        con el fin de facilitar el procesamiento de los datos
        """

        # Paso 1: Estandarizar palabras reemplazando sinónimos
        self.data['AbtractClean'] = self.data['Abstract'].apply(self.reemplazar_sinonimos)
        
        self.data['AbtractClean']=self.data['AbtractClean'].apply( lambda x : str(x).lower() )

        #direccion del nuevo archivo
        base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        file_path_data = os.path.join(base_dir, 'data', 'dataNew.csv')
        
        #generar el nuevo archivo
        self.data.to_csv(file_path_data,index=False)





    #construir una matriz de frecuencia de palabras
    def realizar_matriz_frecuencia(self):
        """
        extraer la columna de abstract y aplicar un conteo de palabras usando la libreria countvectorizer.
        se realiza la configuracion para tener en cuenta no solo palabras si no frases
        """

        self.data
        self.palabras_especiales
        
        # Obtener lista de palabras o frases que queremos buscar en los abstracts
        vocabulario_interes = self.palabras_especiales['Palabra'].tolist()

        # Convierte todo el vocabulario a minúsculas
        vocabulario_interes = [palabra.lower() for palabra in vocabulario_interes]


        # Configuración del vectorizador
        # Usamos CountVectorizer para contar ocurrencias de palabras/frases
        # - lowercase=True para ignorar mayúsculas/minúsculas
        # - ngram_range=(1,3) permite encontrar frases de hasta 3 palabras
        vectorizer = CountVectorizer(
            vocabulary=vocabulario_interes, 
            lowercase=True, 
            ngram_range=(1, 3)
        )



        # Análisis de frecuencia
        # Transformar el texto de los abstracts en una matriz de frecuencias
        matriz_frecuencia = vectorizer.fit_transform(self.data['AbtractClean'])
        
        # Crear DataFrame para mejor visualización
        # Convertimos la matriz a DataFrame usando los nombres de las palabras como columnas
        matriz_frecuencia_df = pd.DataFrame(
            matriz_frecuencia.toarray(),
            columns=vectorizer.get_feature_names_out()
        )

        # Mostrar resultados
        print(matriz_frecuencia_df)

        self.generar_nube_palabras(vectorizer, matriz_frecuencia)






    #generar una nube de palabras
    def generar_nube_palabras(self,vectorizer,matriz_frecuencia):
        """
            Consturir una nube de palabras con base en la matriz de frecuencia generada

            parametros:
                vectorizer: contiene datos especificos del vectorizador con el que se genero la matriz
                matriz_frecuencia: contiene los datos resultandtes de cada una de las palabras
        """
        # Obtener las palabras y sus frecuencias
        frecuencia_palabras = dict(zip(vectorizer.get_feature_names_out(), matriz_frecuencia.sum(axis=0).A1))

        # Generar la nube de palabras
        wordcloud = WordCloud(width=800,max_words=100, height=400, background_color='white').generate_from_frequencies(frecuencia_palabras)

        # Mostrar la nube de palabras
        plt.figure(figsize=(10, 5))
        plt.imshow(wordcloud, interpolation='bilinear')
        plt.axis('off')
        plt.show()




    # Iniciar ejecución del procesamiento
    def iniciar_ejecucion(self):
        """
        Procesar la data según los pasos definidos. el objetivo es estructurar y estandarizar los abstract para un correcto 
        procesamiento de los datos ademas de la facilitacion:
        1. Reemplazar sinónimos en la data con palabras principales.
        2. Generar la matriz de frecuencia de palabras específicas.
        3. Imprimir resultados y generar una nube de palabras.
        """
        # Cargar base de datos bibliográfica
        self.unificar_sinonimos()

        # generar una matriz de frecuencia 
        self.realizar_matriz_frecuencia()




#objeto = Frecuencia()

#objeto.iniciar_ejecucion()
