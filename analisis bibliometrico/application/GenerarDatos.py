import pandas as pd
import random

# Lista de 50 países
paises = [
    "México", "Argentina", "Colombia", "Perú", "Chile", "España", "Brasil", "Uruguay", "Paraguay", "Venezuela",
    "Estados Unidos", "Canadá", "Alemania", "Francia", "Italia", "Reino Unido", "Japón", "China", "India", "Rusia",
    "Australia", "Nueva Zelanda", "Sudáfrica", "Egipto", "Nigeria", "Turquía", "Arabia Saudita", "Irán", "Pakistán",
    "Filipinas", "Indonesia", "Malasia", "Tailandia", "Vietnam", "Corea del Sur", "Israel", "Grecia", "Portugal",
    "Noruega", "Suecia", "Finlandia", "Dinamarca", "Suiza", "Austria", "Bélgica", "Países Bajos", "Polonia", "Hungría",
    "República Checa", "Rumania"
]

# Lista de tipos con probabilidades ajustadas
tipos = ["Article", "Conference", "Book"]
pesos = [0.7, 0.2, 0.1]  # Article tiene más peso que Conference y Book

# Ruta del archivo CSV
ruta_csv = r"C:\Users\brahi\Documents\Proyecto analisis\analisis bibliometrico\data\data.csv"

# Cargar el archivo CSV en un DataFrame
df = pd.read_csv(ruta_csv)

# Crear una columna 'país' con valores aleatorios de la lista de países
#df["País"] = [random.choice(paises) for _ in range(len(df))]

# Reemplazar los valores 'Null' en la columna 'Cited by' con números aleatorios entre 0 y 250
#df["Cited by"] = df["Cited by"].apply(lambda x: random.randint(0, 250) if x == "Null" else x)

# Crear una nueva columna 'Tipo' con valores aleatorios de la lista de tipos, con pesos
df["Tipo"] = [random.choices(tipos, weights=pesos, k=1)[0] for _ in range(len(df))]

# Guardar el DataFrame de nuevo en el archivo CSV
df.to_csv(ruta_csv, index=False)



