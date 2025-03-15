def calcular_temperatura_promedio(temperaturas):
    """
    Esta función calcula la temperatura promedio de cada ciudad durante un período de tiempo.

    Parámetros:
    temperaturas (diccionario): Un diccionario donde la clave es el nombre de la ciudad y el valor es una lista de temperaturas semanales.

    Retorna:
    diccionario: Un diccionario donde la clave es el nombre de la ciudad y el valor es la temperatura promedio de esa ciudad.
    """
    promedios = {}

    for ciudad, temps in temperaturas.items():
        # Calculamos la temperatura promedio para cada ciudad
        promedio = sum(temps) / len(temps)
        promedios[ciudad] = promedio

    return promedios


# Temperaturas de Cuenca, Loja y Yantzaza durante 4 semanas
temperaturas_ciudades = {
    'Cuenca': [18, 19, 17, 18],
    'Loja': [20, 21, 19, 22],
    'Yantzaza': [23, 24, 22, 25]
}

# Llamamos a la función y mostramos los resultados
promedios = calcular_temperatura_promedio(temperaturas_ciudades)
print(promedios)
