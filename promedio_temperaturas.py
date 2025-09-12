# funcion_promedio_temperaturas.py
"""
Función para calcular el promedio de temperaturas por ciudad y semana.
Autor: Christopher Rueda
"""

def calcular_promedios(ciudades, temperaturas):
    """
    Calcula los promedios de temperatura por ciudad y por semana.

    Parámetros:
        ciudades (list of str): nombres de las ciudades.
        temperaturas (list): matriz 3D [ciudad][semana][día].

    Retorna:
        dict: { ciudad: [prom_sem1, prom_sem2, ...], ... }
    """
    promedios = {}

    for i, ciudad in enumerate(ciudades):
        promedios[ciudad] = []
        # temperaturas[i] es la lista de semanas para la ciudad i
        for semana in temperaturas[i]:
            if not semana:  # lista vacía -> evitar división por 0
                promedios[ciudad].append(None)
            else:
                promedio_semana = sum(semana) / len(semana)
                promedios[ciudad].append(promedio_semana)

    return promedios


# Prueba rápida: datos de ejemplo (3 ciudades, 4 semanas, 7 días)
if __name__ == "__main__":
    ciudades = ["Quito", "Guayaquil", "Cuenca"]
    temperaturas = [
        [  # Quito - 4 semanas
            [20,22,19,18,21,23,20],
            [21,22,20,19,18,21,22],
            [19,21,20,20,22,23,21],
            [20,21,19,18,22,22,21]
        ],
        [  # Guayaquil
            [28,30,31,29,28,27,30],
            [29,30,32,31,30,29,28],
            [30,31,29,30,32,31,29],
            [28,29,30,28,27,29,30]
        ],
        [  # Cuenca
            [15,17,16,15,14,18,16],
            [16,17,15,14,15,17,18],
            [15,16,15,16,17,18,16],
            [14,15,16,14,15,17,16]
        ]
    ]

    resultados = calcular_promedios(ciudades, temperaturas)
    for ciudad, proms in resultados.items():
        print(f"\nCiudad: {ciudad}")
        for idx, prom in enumerate(proms, start=1):
            print(f"  Semana {idx}: {prom:.2f}°C")
