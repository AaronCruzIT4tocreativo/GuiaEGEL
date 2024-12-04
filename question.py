import os
import json

carpeta_entrada = "./questions"
carpeta_salida = "./out_questions"

# Crear la carpeta de salida si no existe
os.makedirs(carpeta_salida, exist_ok=True)

# Lista para combinar todos los elementos de todos los archivos
todos_los_elementos = []

# Procesar cada archivo en la carpeta
for archivo in os.listdir(carpeta_entrada):
    if archivo.endswith(".json"):
        ruta_entrada = os.path.join(carpeta_entrada, archivo)
        try:
            with open(ruta_entrada, "r", encoding="utf-8") as f:
                data = json.load(f)

            if isinstance(data, list):
                for item in data:
                    if 'imageName' in item:
                        try:
                            # Convertir 'imageName' a 'questionIndex' como número
                            item['questionIndex'] = int(item.pop('imageName'))
                            todos_los_elementos.append(item)
                        except ValueError:
                            print(f"Error en archivo '{archivo}': valor no convertible: {item['imageName']}")
                    else:
                        print(f"Advertencia: Elemento sin 'imageName' en archivo '{archivo}'.")

            else:
                print(f"El archivo '{archivo}' no contiene un array en el nivel raíz.")
        except json.JSONDecodeError:
            print(f"El archivo '{archivo}' no es un JSON válido.")
        except Exception as e:
            print(f"Error inesperado en archivo '{archivo}': {e}")

# Ordenar todos los elementos combinados por 'questionIndex' (de mayor a menor)
todos_los_elementos_ordenados = sorted(
    todos_los_elementos, key=lambda x: x['questionIndex'], reverse=True
)

# Dividir en grupos de 5 y guardar
for i in range(0, len(todos_los_elementos_ordenados), 5):
    grupo = todos_los_elementos_ordenados[i:i+5]
    nombre_salida = f"grupo_{i//5 + 1}.json"
    ruta_salida = os.path.join(carpeta_salida, nombre_salida)

    with open(ruta_salida, "w", encoding="utf-8") as salida:
        json.dump(grupo, salida, indent=4, ensure_ascii=False)

print(f"Procesamiento completo. Archivos generados en '{carpeta_salida}'.")
