# Fundamentos de Programación (213022)
# Fase 5 - Problema 3: Reabastecimiento de inventario

def calcular_cantidad_a_pedir(stock_actual, stock_minimo):
    if stock_actual < stock_minimo:
        return stock_minimo - stock_actual
    return 0


# Cada fila guarda código, nombre, stock actual y stock mínimo.
inventario = [
    ["A01", "Cuaderno", 4, 10],
    ["A02", "Lápiz", 15, 10],
    ["A03", "Borrador", 8, 8],
    ["A04", "Regla", 0, 5],
    ["A05", "Marcador", 9, 10],
]

print("Lista de reabastecimiento (unidades)")
for articulo in inventario:
    nombre = articulo[1]
    stock_actual = articulo[2]
    stock_minimo = articulo[3]
    cantidad = calcular_cantidad_a_pedir(stock_actual, stock_minimo)
    print(f"{nombre}: {cantidad}")
