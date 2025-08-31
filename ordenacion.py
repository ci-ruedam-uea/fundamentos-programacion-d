# Programa 2: Ordenación de una fila de una matriz (Bubble Sort)

matriz = [
    [9, 3, 7],
    [5, 2, 8],
    [6, 4, 1]
]

def bubble_sort(fila):
    n = len(fila)
    for i in range(n):
        for j in range(0, n-i-1):
            if fila[j] > fila[j+1]:
                fila[j], fila[j+1] = fila[j+1], fila[j]
    return fila

# Elegimos la fila que queremos ordenar (ejemplo: fila 1 -> segunda fila)
fila_a_ordenar = 1

print("Matriz original:")
for fila in matriz:
    print(fila)

# Ordenamos la fila seleccionada
matriz[fila_a_ordenar] = bubble_sort(matriz[fila_a_ordenar])

print("\nMatriz con la fila ordenada:")
for fila in matriz:
    print(fila)
