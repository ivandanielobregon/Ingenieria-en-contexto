carrito_de_compras = []

def agregar_producto(carrito, nombre, precio, cantidad):
    for producto in carrito:
        if producto['nombre'] == nombre:
            producto['cantidad'] += cantidad
            print(f"Cantidad actualizada para '{nombre}'. Nueva cantidad: {producto['cantidad']}")
            return
    carrito.append({"nombre": nombre, "precio": precio, "cantidad": cantidad})
    print(f"'{nombre}' (x{cantidad}) añadido al carrito.")

def calcular_subtotal(carrito):
    subtotal = 0
    for producto in carrito:
        subtotal += producto['precio'] * producto['cantidad']
    return subtotal

def calcular_total_con_descuento(carrito, porcentaje_descuento=0):
    subtotal = calcular_subtotal(carrito)
    if 0 <= porcentaje_descuento <= 100:
        descuento = subtotal * (porcentaje_descuento / 100)
        total_final = subtotal - descuento
        print(f"Subtotal: ${subtotal:.2f}")
        print(f"Descuento aplicado ({porcentaje_descuento}%): ${descuento:.2f}")
        print(f"Total a pagar: ${total_final:.2f}")
        return total_final
    else:
        print("El porcentaje de descuento debe estar entre 0 y 100.")
        return subtotal
agregar_producto(carrito_de_compras, "Camisa", 25000, 2)
agregar_producto(carrito_de_compras, "Pantalón", 40000, 1)
agregar_producto(carrito_de_compras, "Camisa", 15000, 1) 
agregar_producto(carrito_de_compras, "Zapatos", 60000, 1)

print("\nContenido actual del carrito:")
for item in carrito_de_compras:
    print(f"- {item['nombre']}: ${item['precio']:.2f} x {item['cantidad']}")

print("\nCalculando total sin descuento:")
calcular_total_con_descuento(carrito_de_compras)

print("\nCalculando total con 10% de descuento:")
calcular_total_con_descuento(carrito_de_compras, 10) 