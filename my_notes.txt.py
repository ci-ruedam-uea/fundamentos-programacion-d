# trabajo_archivos.py
# Autor: Christopher Rueda
# Descripción: Ejemplo de escritura y lectura de archivos de texto en Python.
# Objetivo: Practicar operaciones básicas con archivos (write, readline, close).

# --------------------------
# ESCRITURA EN ARCHIVO
# --------------------------

# Abrimos (o creamos) el archivo 'my_notes.txt' en modo escritura ("w") con codificación UTF-8
with open("my_notes.txt", "w", encoding="utf-8") as archivo:
    archivo.write("Primera nota: Hoy estoy practicando Python con archivos.\n")
    archivo.write("Segunda nota: Me gusta aprender paso a paso.\n")
    archivo.write("Tercera nota: GitHub es útil para guardar mis proyectos.\n")

# --------------------------
# LECTURA DEL ARCHIVO
# --------------------------

# Abrimos el archivo en modo lectura con codificación UTF-8
with open("my_notes.txt", "r", encoding="utf-8") as archivo:
    print("Contenido del archivo:\n")
    linea = archivo.readline()  # Lee la primera línea

    while linea:  # Mientras haya texto que leer
        print(linea.strip())  # strip() elimina saltos de línea extra
        linea = archivo.readline()  # Lee la siguiente línea
