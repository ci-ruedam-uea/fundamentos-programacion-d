# Programa 1: Búsqueda en Arreglo Multidimensional

# Definimos una matriz 3x3
matriz = [
    [4, 7, 9],
    [2, 5, 8],
    [1, 3, 6]
]

def buscar_valor(matriz, valor):
    for i in range(len(matriz)):          # Recorremos filas
        for j in range(len(matriz[i])):   # Recorremos columnas
            if matriz[i][j] == valor:
                return (i, j)  # Retorna la posición (fila, columna)
    return None

# Valor a buscar
valor_buscado = 5
resultado = buscar_valor(matriz, valor_buscado)

print("Matriz:")
for fila in matriz:
    print(fila)

if resultado:
    print(f"\n✅ El valor {valor_buscado} se encontró en la posición: fila {resultado[0]}, columna {resultado[1]}")
else:
    print(f"\n❌ El valor {valor_buscado} no se encontró en la matriz")
