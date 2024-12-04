import os
import json

# Función para convertir un rango "100-105" en un array de números [100, 101, 102, 103, 104, 105]
def parse_range(range_str):
    parts = range_str.split('-')
    start = int(parts[0])
    
    if len(parts) == 1:
        return [start]
    
    end = int(parts[1])
    return list(range(start, end + 1))

# Función para leer los archivos JSON en la carpeta
def read_json_files(directory):
    all_data = []
    for file_name in os.listdir(directory):
        if file_name.endswith('.json'):
            with open(os.path.join(directory, file_name), 'r', encoding='utf-8') as file:
                all_data.extend(json.load(file))
    return all_data

# Función para procesar los datos y extraer los rangos de números en 'imageIndex'
def process_image_indexes(data):
    for item in data:
        # Procesamos la propiedad 'imageIndex', la cual puede ser un rango o una lista de rangos
        ranges = item['imageIndex'].split(',')
        item['imageIndexes'] = []
        for range_str in ranges:
            item['imageIndexes'].extend(parse_range(range_str.strip()))
    return data

# Función para ordenar los datos por los números extraídos de imageIndex
def sort_data_by_image_index(data):
    return sorted(data, key=lambda x: min(x['imageIndexes']))

# Función para guardar los datos en un archivo JSON
def save_to_json_file(data, output_file):
    with open(output_file, 'w', encoding='utf-8') as file:
        json.dump(data, file, indent=2, ensure_ascii=False)  # Asegura que los caracteres no sean escapados

# Función principal
def main():
    directory = './questions'  # Directorio donde están los archivos JSON
    base_output_file = './sorted/salida_'  # Prefijo para los archivos de salida

    # Leer y procesar los datos
    data = read_json_files(directory)
    processed_data = process_image_indexes(data)
    sorted_data = sort_data_by_image_index(processed_data)

    # Agrupar los datos en bloques de 5 elementos
    grouped_data = [sorted_data[i:i + 5] for i in range(0, len(sorted_data), 5)]

    # Guardar cada bloque de 5 datos en un archivo separado
    for index, group in enumerate(grouped_data, start=1):
        output_file = f"{base_output_file}{index}.json"
        save_to_json_file(group, output_file)
        print(f'Datos procesados y guardados en {output_file}')

if __name__ == "__main__":
    main()
