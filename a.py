import os
import json

def update_answers(source_folder, target_folder, output_folder):
    # Crear la carpeta de salida si no existe
    os.makedirs(output_folder, exist_ok=True)

    # Obtener los nombres de archivos fuente y destino
    source_files = sorted([f for f in os.listdir(source_folder) if f.startswith("A") and f.endswith(".json")])
    target_files = sorted([f for f in os.listdir(target_folder) if f.startswith("salida") and f.endswith(".json")])

    # Imprimir información sobre los archivos encontrados
    print(f"Archivos fuente encontrados: {source_files}")
    print(f"Archivos destino encontrados: {target_files}")

    # Verificar si los números de archivos coinciden
    if len(source_files) != len(target_files):
        print(f"El número de archivos fuente ({len(source_files)}) y destino ({len(target_files)}) no coincide.")
        print("Verifica que ambos directorios tengan el mismo número de archivos con los nombres correctos.")
        return

    # Iterar sobre los archivos correspondientes
    for source_file, target_file in zip(source_files, target_files):
        # Cargar el archivo fuente
        with open(os.path.join(source_folder, source_file), "r", encoding="utf-8") as src_file:
            source_data = json.load(src_file)

        # Crear un diccionario para búsqueda rápida de respuestas por índice
        source_dict = {item["index"]: item for item in source_data}

        # Cargar el archivo de destino
        with open(os.path.join(target_folder, target_file), "r", encoding="utf-8") as tgt_file:
            target_data = json.load(tgt_file)

        # Actualizar las respuestas y explicaciones en las opciones del destino
        for question in target_data:
            # Buscar respuesta en las opciones
            answer_found = False
            for option in question["options"]:
                for src_index, src_item in source_dict.items():
                    if option["text"] == src_item["answer"]:
                        # Agregar la respuesta y explicación
                        question["answer"] = {
                            "index": src_item["index"],
                            "text": src_item["answer"],
                            "explanation": src_item["explanation"]
                        }
                        answer_found = True
                        break
                if answer_found:
                    break
            
            # Si no se encontró una respuesta seleccionada, asignamos la primera opción como respuesta
            if not answer_found:
                # Suponemos que la respuesta correcta está en la primera opción si no hay una seleccionada
                question["answer"] = {
                    "index": 0,
                    "text": question["options"][0]["text"],  # Tomamos el texto de la primera opción
                    "explanation": "Explicación no proporcionada, ya que no se seleccionó una respuesta."
                }

        # Guardar el archivo actualizado en la carpeta de salida
        output_file_path = os.path.join(output_folder, target_file)
        with open(output_file_path, "w", encoding="utf-8") as output_file:
            json.dump(target_data, output_file, indent=4, ensure_ascii=False)

    print(f"Archivos actualizados guardados en {output_folder}")

# Carpetas de origen y destino
source_folder = "answers_json"  # Carpeta con las respuestas (e.g., A1.json)
target_folder = "sorted"  # Carpeta con las preguntas (e.g., salida_1.json)
output_folder = "sorted_answers"  # Carpeta donde se guardarán los resultados

update_answers(source_folder, target_folder, output_folder)
