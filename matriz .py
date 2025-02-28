# Definimos la matriz bidimensional (3x3)
matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Función para buscar un valor en la matriz
def buscar_valor(matriz, valor):
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] == valor:
                return i, j  # Retorna las coordenadas (fila, columna)
    return None  # Si no se encuentra el valor

# Definir el valor a buscar
valor_a_buscar = 2

# Llamamos a la función para buscar el valor
resultado = buscar_valor(matriz, valor_a_buscar)

# Mostrar el resultado
if resultado:
    fila, columna = resultado
    print(f"Valor {valor_a_buscar} encontrado en la posición ({fila}, {columna}) de la matriz.")
else:
    print(f"Valor {valor_a_buscar} no encontrado en la matriz.")
