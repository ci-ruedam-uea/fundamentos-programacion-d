# informacion_personal.py
# Ejemplo: Trabajando con diccionarios en Python
# Autor: Christopher Rueda
# Comentarios: este script crea un diccionario, permite ingresar datos
# desde una interfaz gráfica, modifica valores, añade claves si no existen,
# elimina una clave y muestra el resultado final.

import tkinter as tk
from tkinter import messagebox

# Lista para guardar las personas
personas = []


def agregar_persona():
    nombre = entry_nombre.get()
    edad = entry_edad.get()
    ciudad = entry_ciudad.get()
    profesion = entry_profesion.get()
    telefono = entry_telefono.get()

    if nombre and edad and ciudad and profesion and telefono:
        try:
            edad = int(edad)  # validar que la edad sea número
        except ValueError:
            messagebox.showerror("Error", "La edad debe ser un número")
            return

        # Crear diccionario de persona
        persona = {
            "nombre": nombre,
            "edad": edad,
            "ciudad": ciudad,
            "profesion": profesion,
            "telefono": telefono
        }

        # Modificar la ciudad (ejemplo: agregar un texto para demostrar el cambio)
        persona["ciudad"] = persona["ciudad"] + " (actualizada)"

        # Eliminar la clave "edad" como pide la tarea
        if "edad" in persona:
            del persona["edad"]

        # Guardar en la lista
        personas.append(persona)

        # Mostrar en el cuadro de texto
        lista_personas.insert(tk.END, f"{persona}")

        # Limpiar entradas
        entry_nombre.delete(0, tk.END)
        entry_edad.delete(0, tk.END)
        entry_ciudad.delete(0, tk.END)
        entry_profesion.delete(0, tk.END)
        entry_telefono.delete(0, tk.END)

        # Mensaje de estado
        texto_estado.set(f"Se agregó a {nombre}. Total personas: {len(personas)}")
    else:
        messagebox.showwarning("Atención", "Por favor completa todos los campos")


def procesar():
    if personas:
        resumen = "\n".join([str(p) for p in personas])
        messagebox.showinfo("Procesamiento", f"Diccionarios finales:\n\n{resumen}")
    else:
        messagebox.showwarning("Atención", "No hay personas registradas")


# Ventana principal
ventana = tk.Tk()
ventana.title("Registro de Personas con Diccionarios")
ventana.geometry("500x550")

# Etiquetas y entradas
tk.Label(ventana, text="Nombre:").grid(row=0, column=0, padx=5, pady=5, sticky="e")
entry_nombre = tk.Entry(ventana, width=30)
entry_nombre.grid(row=0, column=1, padx=5, pady=5)

tk.Label(ventana, text="Edad:").grid(row=1, column=0, padx=5, pady=5, sticky="e")
entry_edad = tk.Entry(ventana, width=30)
entry_edad.grid(row=1, column=1, padx=5, pady=5)

tk.Label(ventana, text="Ciudad:").grid(row=2, column=0, padx=5, pady=5, sticky="e")
entry_ciudad = tk.Entry(ventana, width=30)
entry_ciudad.grid(row=2, column=1, padx=5, pady=5)

tk.Label(ventana, text="Profesión:").grid(row=3, column=0, padx=5, pady=5, sticky="e")
entry_profesion = tk.Entry(ventana, width=30)
entry_profesion.grid(row=3, column=1, padx=5, pady=5)

tk.Label(ventana, text="Teléfono:").grid(row=4, column=0, padx=5, pady=5, sticky="e")
entry_telefono = tk.Entry(ventana, width=30)
entry_telefono.grid(row=4, column=1, padx=5, pady=5)

# Botones
tk.Button(ventana, text="Agregar Persona", command=agregar_persona).grid(row=5, column=0, columnspan=2, pady=10)
tk.Button(ventana, text="Procesar Todo", command=procesar).grid(row=6, column=0, columnspan=2, pady=5)

# Lista de personas
tk.Label(ventana, text="Personas Registradas (diccionarios):").grid(row=7, column=0, columnspan=2)
lista_personas = tk.Listbox(ventana, width=60, height=10)
lista_personas.grid(row=8, column=0, columnspan=2, padx=5, pady=5)

# Estado
texto_estado = tk.StringVar()
tk.Label(ventana, textvariable=texto_estado, fg="blue").grid(row=9, column=0, columnspan=2, pady=5)

ventana.mainloop()
