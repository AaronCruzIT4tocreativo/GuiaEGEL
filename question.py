import os
import json

# Ruta de la carpeta donde están los archivos .json
carpeta = "./questions"
# carpeta = "./questions/drive/GITG"

# Recorremos cada archivo en la carpeta
for archivo in os.listdir(carpeta):
    if archivo.endswith(".json"):  # Solo procesar archivos .json
        ruta_archivo = os.path.join(carpeta, archivo)
        
        # Abrir y leer el contenido del archivo
        with open(ruta_archivo, "r", encoding="utf-8") as f:
            try:
                data = json.load(f)  # Cargar el contenido del archivo como JSON
                if isinstance(data, list):  # Comprobar si el contenido es un array
                    print(f"El archivo '{archivo}' tiene un tamaño de {len(data)} elementos.")
                else:
                    print(f"El archivo '{archivo}' no contiene un array en el nivel raíz.")
            except json.JSONDecodeError:
                print(f"El archivo '{archivo}' no es un JSON válido.")
