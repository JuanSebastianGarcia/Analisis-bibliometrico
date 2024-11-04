import pandas as pd

# Ruta del archivo .bib
bib_file_path = r"C:\Users\brahi\Downloads\ScientDirect.bib"
output_csv_path = r"C:\Users\brahi\Documents\Proyecto analisis\analisis bibliometrico\data\ScientDirect_converted.csv"

# Diccionario para almacenar las entradas
entries_dict = {}

# Leer el archivo .bib línea por línea
with open(bib_file_path, 'r', encoding='utf-8') as bib_file:
    entry_data = {}
    entry_key = None
    for line in bib_file:
        # Detectar inicio de una entrada
        if line.startswith('@'):
            entry_type, entry_key = line.split('{', 1)
            entry_key = entry_key.split(',', 1)[0]
            entry_data = {'type': entry_type.strip('@')}  # Crear una nueva entrada

        # Detectar fin de una entrada y agregarla si no está duplicada
        elif line.startswith('}'):
            if entry_key not in entries_dict:
                entries_dict[entry_key] = entry_data
            entry_data = {}

        # Procesar cada campo de la entrada
        else:
            if '=' in line:
                key, value = line.split('=', 1)
                entry_data[key.strip()] = value.strip().strip('{},')

# Convertir el diccionario de entradas a un DataFrame de pandas
df = pd.DataFrame.from_dict(entries_dict, orient='index')

# Guardar el DataFrame como archivo CSV
df.to_csv(output_csv_path, index=False)

print(f"Archivo CSV generado en: {output_csv_path}")


# Carga el archivo CSV
df = pd.read_csv(r'C:\Users\brahi\Documents\Proyecto analisis\analisis bibliometrico\data\ScientDirect_converted.csv')

# Quita 'https://doi.org/' de cada valor en la columna 'doi'
df['doi'] = df['doi'].str.replace('https://doi.org/', '', regex=False)

# Guarda el archivo modificado
df.to_csv(r'C:\Users\brahi\Documents\Proyecto analisis\analisis bibliometrico\data\ScientDirect.csv', index=False)


