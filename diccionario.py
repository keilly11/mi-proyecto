# Crear un diccionario con información ficticia sobre una persona
informacion_personal = {
    "nombre": "Andrea Gómez",  # Nombre ficticio
    "edad": 28,  # Edad ficticia
    "ciudad": "Cuenca",  # Ciudad original
    "profesion": "Arquitecta"  # Profesión original
}

# Acceder y modificar el valor de "ciudad"
informacion_personal["ciudad"] = "Loja"  # Cambio de ciudad

# Agregar una nueva clave-valor para "profesion"
informacion_personal["profesion"] = "Diseñadora de Interiores"  # Actualización de profesión

# Verificar si "telefono" existe, si no, agregarlo
if "telefono" not in informacion_personal:
    informacion_personal["telefono"] = "0987654321"  # Número de teléfono ficticio

# Eliminar la clave "edad" del diccionario, ya que no es necesaria
del informacion_personal["edad"]

# Imprimir el diccionario final con los cambios realizados
print(informacion_personal)

# Instrucción final: Subir este código a GitHub y adjuntar el enlace en la plataforma de la asignatura.
