import funciones

carrito = []
carritoV = []

print("SUPERMERCADO".center(50, "-"))

while True:
    print("\n1. Agregar Producto")
    print("2. Eliminar Producto")
    print("3. Vender Producto")
    print("4. Factura")
    print("5. Salir")

    op = input("Ingrese la opción: ")
    print()

    if op == "1":
        nombre = input("Ingrese nombre del producto: ")
        valor = float(input("Ingrese valor del producto: "))
        carrito = funciones.agregar(nombre, valor, carrito)

    elif op == "2":
        nombre = input("Ingrese nombre del producto: ")
        carrito = funciones.quitar(nombre, carrito)

    elif op == "3":
        nombre = input("Ingrese nombre del producto: ")
        valor = float(input("Ingrese valor del producto: "))
        carritoV = funciones.vender(nombre, valor, carritoV)

    elif op == "4":
        funciones.factura(carrito, carritoV)

    elif op == "5":
        print("Buen dia.\n")
        break
    
    else:
        print("Opción inválida\n")
