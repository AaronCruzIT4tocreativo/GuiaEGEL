import os
import json
from collections import defaultdict

# Ruta de la carpeta donde están los archivos .json
carpeta_entrada = "./out_questions"
carpeta_salida = "./sorted_questions"

# Crear la carpeta de salida si no existe
os.makedirs(carpeta_salida, exist_ok=True)

# Lista para combinar todos los valores de 'imageIndex'
todos_los_elementos = []

# Función para dividir un rango en números individuales
def expandir_rango(rango):
    if "-" in rango:
        inicio, fin = map(int, rango.split("-"))
        return list(range(inicio, fin + 1))
    else:
        return [int(rango)]  # Si no es un rango, convertir a entero

# Procesar cada archivo en la carpeta
for archivo in os.listdir(carpeta_entrada):
    if archivo.endswith(".json"):
        ruta_entrada = os.path.join(carpeta_entrada, archivo)
        try:
            with open(ruta_entrada, "r", encoding="utf-8") as f:
                data = json.load(f)

            if isinstance(data, list):
                for item in data:
                    if 'imageIndex' in item:
                        try:
                            valores = expandir_rango(item['imageIndex'])
                            # Crear los items con la propiedad 'questionIndex'
                            for valor in valores:
                                item['questionIndex'] = valor
                                todos_los_elementos.append(item.copy())  # Guardamos una copia de cada item
                        except ValueError:
                            print(f"Error en archivo '{archivo}': valor no convertible: {item['imageIndex']}")
            else:
                print(f"El archivo '{archivo}' no contiene un array en el nivel raíz.")
        except json.JSONDecodeError:
            print(f"El archivo '{archivo}' no es un JSON válido.")
        except Exception as e:
            print(f"Error inesperado en archivo '{archivo}': {e}")

# Agrupar los elementos por 'imageIndex' (convertido a 'questionIndex')
grupos_por_index = defaultdict(list)

for item in todos_los_elementos:
    grupos_por_index[item['imageIndex']].append(item)

# Guardar los elementos en archivos separados por 'imageIndex' y en grupos de 5
for image_index, elementos in grupos_por_index.items():
    # Dividir los elementos en grupos de 5
    for i in range(0, len(elementos), 5):
        grupo = elementos[i:i+5]
        nombre_salida = f"{image_index}_{i//5 + 1}.json"
        ruta_salida = os.path.join(carpeta_salida, nombre_salida)
        with open(ruta_salida, "w", encoding="utf-8") as salida:
            json.dump(grupo, salida, indent=4, ensure_ascii=False)

print(f"Archivos generados y guardados en '{carpeta_salida}'.")
