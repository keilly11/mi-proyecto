def calcular_descuento(monto_total, porcentaje_descuento=10):
    """
    Esta función calcula el descuento de una compra.

    Parámetros:
    - monto_total: El valor total de la compra.
    - porcentaje_descuento: El porcentaje de descuento a aplicar (por defecto es 10%).

    Retorna:
    - El monto del descuento calculado.
    """
    descuento = (monto_total * porcentaje_descuento) / 100
    return descuento


# Definir montos de compra
monto1 = 100  # Primera compra
monto2 = 200  # Segunda compra con un porcentaje diferente
porcentaje_personalizado = 15  # Descuento personalizado

# Calcular descuentos

descuento1 = calcular_descuento(monto1)  # Usando el descuento por defecto (10%)
descuento2 = calcular_descuento(monto2, porcentaje_personalizado)  # Usando un 15% de descuento

# Mostrar los resultados
print(f"Compra 1: Monto total: ${monto1}, Descuento: ${descuento1}, Monto final: ${monto1 - descuento1}")
print(f"Compra 2: Monto total: ${monto2}, Descuento: ${descuento2}, Monto final: ${monto2 - descuento2}")
