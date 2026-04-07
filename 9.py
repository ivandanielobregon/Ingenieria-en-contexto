def agrupar_productos_por_categoria(lista_productos_categorias):
    productos_por_categoria = {}
    for producto, categoria in lista_productos_categorias:
        if categoria not in productos_por_categoria:
            productos_por_categoria[categoria] = [] 
        productos_por_categoria[categoria].append(producto) 
    return productos_por_categoria
listado_ejemplo = [
    ("Manzanas", "Frutas"),
    ("Leche", "Lácteos"),
    ("Peras", "Frutas"),
    ("Yogur", "Lácteos"),
    ("Pan", "Panadería"),
    ("Naranjas", "Frutas"),
    ("Queso", "Lácteos")
]
productos_agrupados = agrupar_productos_por_categoria(listado_ejemplo)

print("Listado original:", listado_ejemplo)
print("\nProductos agrupados por categoría:", productos_agrupados)