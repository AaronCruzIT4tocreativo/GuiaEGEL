# Lista de números
numeros = [
    1, 2, 3, 4, 5,
    6, 7, 8, 9, 10,
    11, 12, 13, 14, 15, 16,
    17, 18, 19, 20, 21, 22,
    23, 24, 25, 26, 27, 28, 29, 30, 31,
    32, 33, 34, 35, 36, 37, 38, 39,
    40, 41, 42, 43, 44,
    45, 46, 47, 48, 49, 50, 51, 52, 53,
    54, 55, 56, 57, 58, 59, 60, 61, 62, 63,
    105, 106, 107, 108, 109, 110, 111,
    112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123,
    124, 125, 126, 127, 128, 129, 130, 131, 132, 133,
    134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146,
    147, 148, 149, 150, 151, 152, 153, 154, 155,
    156, 157, 158, 159, 160,
    161, 162, 163, 164, 165,
    166, 167, 168, 169, 170,
    171, 172, 173, 174, 175,
    176, 177, 178, 179, 180
]

# Rango esperado
rango_completo = set(range(1, 194))

# Convertir la lista en un conjunto para eliminar duplicados y compararla
numeros_unicos = set(numeros)

# Verificar duplicados
duplicados = sorted(set([num for num in numeros if numeros.count(num) > 1]))

# Encontrar números faltantes
faltantes = sorted(rango_completo - numeros_unicos)

# Resultados
print(f"Duplicados: {duplicados}")
print(f"Faltantes: {faltantes}")