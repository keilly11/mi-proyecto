# Escritura en el archivo my_notes.txt
# Abrimos el archivo en modo escritura ('w') para crear o sobrescribir el archivo
with open('my_notes.txt', 'w') as file:
    # Escribimos tres líneas de notas personales
    file.write("Hoy fue un día productivo.\n")
    file.write("Aprendí cómo trabajar con archivos en Python.\n")
    file.write("Necesito practicar más para mejorar mis habilidades.\n")

# Lectura del archivo my_notes.txt
# Abrimos el archivo en modo lectura ('r')
with open('my_notes.txt', 'r') as file:
    # Leemos el contenido línea por línea usando readline() en un bucle
    print("Contenido del archivo:")
    while True:
        line = file.readline()
        # Si la línea está vacía, significa que se llegó al final del archivo
        if not line:
            break
        print(line.strip())  # .strip() elimina el salto de línea adicional al imprimir

# El uso de 'with' asegura que los archivos se cierren automáticamente
