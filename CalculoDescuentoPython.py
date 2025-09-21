# Programa: Cálculo de Descuento en Compras
# Autor: Christopher Rueda
# Descripción: Este programa calcula el descuento aplicado a una compra
# utilizando una función con parámetros y valores predeterminados.

# ------------------ Definición de la función ------------------

def calcular_descuento(monto_total, porcentaje_descuento=10):
    """
    Calcula el descuento y devuelve el monto del descuento.

    Parámetros:
    - monto_total (float): El monto total de la compra.
    - porcentaje_descuento (float, opcional): El porcentaje de descuento a aplicar (por defecto 10%).

    Retorna:
    - descuento (float): El monto del descuento calculado.
    """
    descuento = monto_total * (porcentaje_descuento / 100)
    return descuento


# ------------------ Programa principal ------------------

# Ejemplo 1: Usando el descuento por defecto (10%)
monto1 = 100
descuento1 = calcular_descuento(monto1)
monto_final1 = monto1 - descuento1
print(f"Monto de la compra: ${monto1}")
print(f"Descuento aplicado (10%): ${descuento1}")
print(f"Monto final a pagar: ${monto_final1}\n")

# Ejemplo 2: Usando un porcentaje personalizado (20%)
monto2 = 200
descuento2 = calcular_descuento(monto2, 20)
monto_final2 = monto2 - descuento2
print(f"Monto de la compra: ${monto2}")
print(f"Descuento aplicado (20%): ${descuento2}")
print(f"Monto final a pagar: ${monto_final2}")
