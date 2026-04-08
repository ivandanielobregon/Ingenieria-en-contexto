def agregar(nombre, valor, lista):
    producto = (nombre, valor)
    lista.append(producto)
    print("Producto agregado correctamente\n")
    return lista


def quitar(nombre, lista):
    for producto in lista:
        if producto[0] == nombre:
            lista.remove(producto)
            print("Producto eliminado\n")
            return lista
    print("Producto no encontrado\n")
    return lista  


def vender(nombre, valor, lista):
    producto = (nombre, valor)
    lista.append(producto)
    print("Producto vendido\n")
    return lista

def factura(carrito, carritoV):
    total_compra = 0
    total_venta = 0

    print("\n" + "FACTURA".center(40, "-"))

    print("\nProductos comprados:")
    for producto in carrito:
        print(f"{producto[0]} - ${producto[1]}")
        total_compra += producto[1]

    print("\nProductos vendidos:")
    for producto in carritoV:
        print(f"{producto[0]} - ${producto[1]}")
        total_venta += producto[1]

    total_final = total_compra - total_venta

    print("\n" + "-"*40)
    print(f"Total compras: ${total_compra}")
    print(f"Total ventas: ${total_venta}")
    print(f"TOTAL A PAGAR: ${total_final}")
    print("-"*40 + "\n")

    return total_final
