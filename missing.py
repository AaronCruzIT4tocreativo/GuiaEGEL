import os
import json
from collections import Counter

# Ruta de la carpeta donde están los archivos .json
carpeta_entrada = "./out_questions"

# Lista para combinar todos los valores de 'imageIndex'
todos_los_indices = []

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
                            todos_los_indices.extend(valores)
                        except ValueError:
                            print(f"Error en archivo '{archivo}': valor no convertible: {item['imageIndex']}")
            else:
                print(f"El archivo '{archivo}' no contiene un array en el nivel raíz.")
        except json.JSONDecodeError:
            print(f"El archivo '{archivo}' no es un JSON válido.")
        except Exception as e:
            print(f"Error inesperado en archivo '{archivo}': {e}")

# Contar las apariciones de cada número
contador_indices = Counter(todos_los_indices)

# Eliminar duplicados y ordenar los números
todos_los_indices_unicos = sorted(set(todos_los_indices))

# Encontrar los números que faltan en el rango del 1 al 193
todos_los_numeros = set(range(1, 194))
faltantes = sorted(todos_los_numeros - set(todos_los_indices_unicos))

# Mostrar resultados
print(f"Valores únicos encontrados: {todos_los_indices_unicos}")
print(f"Números repetidos y sus frecuencias: {dict(filter(lambda x: x[1] > 1, contador_indices.items()))}")
print(f"Números faltantes del 1 al 193: {faltantes}")
