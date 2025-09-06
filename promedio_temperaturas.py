# Programa: Promedio de temperaturas por ciudad y semana

# Ciudades
ciudades = ["Quito", "Guayaquil", "Cuenca"]

# Días de la semana (7)
dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]

# Semanas (ejemplo: 2 semanas)
num_semanas = 2

# Creamos la matriz 3D [ciudad][semana][día]
# Para simplificar, usamos valores fijos de temperaturas (puedes poner valores reales o aleatorios)
matriz_temperaturas = [
    [   # Quito
        [20, 22, 19, 18, 21, 23, 20],  # Semana 1
        [21, 22, 20, 19, 18, 21, 22]   # Semana 2
    ],
    [   # Guayaquil
        [28, 30, 31, 29, 28, 27, 30],  # Semana 1
        [29, 30, 32, 31, 30, 29, 28]   # Semana 2
    ],
    [   # Cuenca
        [15, 17, 16, 15, 14, 18, 16],  # Semana 1
        [16, 17, 15, 14, 15, 17, 18]   # Semana 2
    ]
]

# Cálculo de promedios usando bucles anidados
for i in range(len(ciudades)):  # Itera sobre ciudades
    ciudad = ciudades[i]
    print(f"\n📍 Ciudad: {ciudad}")
    for j in range(num_semanas):  # Itera sobre semanas
        semana = j + 1
        suma = 0
        for k in range(len(dias)):  # Itera sobre días
            suma += matriz_temperaturas[i][j][k]
        promedio = suma / len(dias)
        print(f"   Semana {semana}: Promedio de temperatura = {promedio:.2f}°C")
