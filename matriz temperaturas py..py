import random

# Definir dimensiones de la matriz
num_ciudades = 3  # Número de ciudades
num_dias = 7       # Días de la semana
num_semanas = 4    # Número de semanas

# Crear matriz 3D con temperaturas aleatorias entre 15 y 35 grados
matriz_temperaturas = [[[random.randint(15, 35) for _ in range(num_dias)]
                         for _ in range(num_semanas)]
                         for _ in range(num_ciudades)]

# Nombres de ciudades
ciudades = [" Cuenca A", " Loja B", "Yantzaza C"]

# Nombres de los días de la semana
dias_semana = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]

# Mostrar las temperaturas generadas
for i, ciudad in enumerate(ciudades):
    print(f"\nTemperaturas para {ciudad}:")
    for semana in range(num_semanas):
        print(f"  Semana {semana + 1}:")
        for dia in range(num_dias):
            print(f"    {dias_semana[dia]}: {matriz_temperaturas[i][semana][dia]}°C")

# Calcular y mostrar el promedio de temperaturas por ciudad y semana
for i, ciudad in enumerate(ciudades):
    print(f"\nPromedio de temperaturas para {ciudad}:")
    for semana in range(num_semanas):
        promedio = sum(matriz_temperaturas[i][semana]) / num_dias
        print(f"  Semana {semana + 1}: {promedio:.2f}°C")

