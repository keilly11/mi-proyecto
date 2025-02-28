# Definimos la matriz bidimensional (3x3)
matriz = [
    [9, 2, 5],
    [8, 7, 3],
    [6, 4, 1]
]

# Función de ordenación (Bubble Sort) para ordenar una fila
def ordenar_fila(fila):
    n = len(fila)
    for i in range(n):
        for j in range(0, n-i-1):
            if fila[j] > fila[j+1]:
                # Intercambiar los elementos si están en el orden incorrecto
                fila[j], fila[j+1] = fila[j+1], fila[j]

# Función para ordenar una fila específica en la matriz
def ordenar_fila_en_matriz(matriz, fila_index):
    # Ordenamos la fila específica
    ordenar_fila(matriz[fila_index])

# Mostrar la matriz original
print("Matriz original:")
for fila in matriz:
    print(fila)

# Elegir la fila a ordenar (por ejemplo, la fila 1 que es la segunda fila)
fila_a_ordenar = 1

# Llamamos a la función para ordenar la fila seleccionada
ordenar_fila_en_matriz(matriz, fila_a_ordenar)

# Mostrar la matriz con la fila ordenada
print("\nMatriz con la fila ordenada:")
for fila in matriz:
    print(fila)
