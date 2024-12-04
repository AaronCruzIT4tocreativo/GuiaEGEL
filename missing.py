import os
import json
import re

# Función para convertir índices a valores numéricos (manejando rangos como "1-5")
def parse_image_index(index):
    if "-" in index:  # Si es un rango
        start, end = map(int, index.split("-"))
        return list(range(start, end + 1))  # Devuelve todos los números del rango
    return [int(index)]  # Si no es un rango, devuelve el número como lista

# Función para leer los archivos JSON en la carpeta e imprimir los imageIndexes ordenados
def print_sorted_image_indexes(directory):
    for file_name in os.listdir(directory):
        if file_name.endswith('.json'):
            file_path = os.path.join(directory, file_name)
            with open(file_path, 'r', encoding='utf-8') as file:
                data = json.load(file)  # Cargamos el contenido del archivo
                if isinstance(data, list):  # Verificamos si es un array
                    print(f"Archivo: {file_name}")
                    image_indexes = []
                    for item in data:
                        if 'imageIndex' in item:
                            image_indexes.extend(parse_image_index(item['imageIndex']))
                    
                    # Ordenar los índices de manera numérica
                    sorted_indexes = sorted(image_indexes)
                    print(f"imageIndexes ordenados: {sorted_indexes}")
                else:
                    print(f"Archivo: {file_name} no contiene un array.")
                print()  # Separador entre archivos

# Función principal
def main():
    directory = './sorted'  # Directorio donde están los archivos JSON
    print_sorted_image_indexes(directory)

if __name__ == "__main__":
    main()
