# Analisis-bibliografico
Proyecto para el análisis bibliográfico de cientos de artículos. Demuestra la capacidad de estructurar y procesar grandes volúmenes de datos bibliográficos, extrayendo información relevante. Es una práctica y demostración del análisis de datos y la interpretación de resultados.



# explicacion de clases y directorios
Aqui se hace una corta explicacion de cada directorio y de las clases para comprender el proyecto

ANALISIS BIBLIOMETRICO
|
|--application  --> Contiene todo el codigo fuente del proyecto
|   |
|   |-- Analisis de algoritmos  --> Contiene una lista de algoritmos de ordenamiento base muy comunes
|   |
|   |--Ordenar --> Esta clase contiene el codigo del algoritmo timsort, modificado para el ordenamiento de los datos que se usaran
|   |               en el proyecto y genera su archivo csv ordenado llamado "dataOrd"
|   |
|   |--Ordenarv2 --> Esta clase contiene el codigo del algoritmo quicksort, modificado para el ordenamiento de los datos que se usaran en 
|   |               el proyecto y genera su archivo csv ordenado llamado "dataOrdv2"
|   |
|   |--Unificacion --> Esta clase contiene el codigo que toma los datos entregados por scopus e IEEE, y los unifica en una sola
|   |               estructura de datos y generando su csv llamdo "data.csv"
|
|--data --> Este directorio contiene todos los archivos csv que son procesados y/o generados por el proyecto.
|   |
|   |--data --> Archivo unificado la adata de scopues e IEEE en la misma estructura
|   |--dataIEEE --> data de la base de datos IEEE
|   |--dataScopues --> data de la base de datos scopus
|   |--dataOrd --> datos unificados y  ordenamos segun un criterio establecido por nosotros. es generado por la clase "Ordenar"
|   |--dataOrdv2 --> datos unificados y  ordenamos segun un criterio establecido por nosotros. es generado por la clase "OrdenarV2"
|
|