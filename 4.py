def calcular_valor_inventario(inventario):
    valor_total = 0
    for producto in inventario:
        valor_producto = producto['precio'] * producto['cantidad']
        valor_total += valor_producto
    return valor_total
inventario_ejemplo = [
    {"nombre": "Laptop", "precio": 1500200, "cantidad": 5},
    {"nombre": "Teclado", "precio": 75000, "cantidad": 20},
    {"nombre": "Mouse", "precio": 65000, "cantidad": 30},
    {"nombre": "Monitor", "precio": 3000000, "cantidad": 10}
]
valor_total_inventario = calcular_valor_inventario(inventario_ejemplo)

print("Inventario actual:", inventario_ejemplo)
print(f"\nEl valor total del inventario es: ${valor_total_inventario:.2f}")