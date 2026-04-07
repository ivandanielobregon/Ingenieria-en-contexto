agenda = {}
def agregar_contacto(agenda, nombre, telefono):
    agenda[nombre] = telefono 
    print(f"Contacto '{nombre}' agregado.")
def buscar_contacto(agenda, nombre):
    if nombre in agenda: 
        print(f"Teléfono de '{nombre}': {agenda[nombre]}")
    else:
        print(f"El contacto '{nombre}' no se encontró.")
def eliminar_contacto(agenda, nombre):
    if nombre in agenda: 
        del agenda[nombre] 
        print(f"Contacto '{nombre}' eliminado.")
    else:
        print(f"El contacto '{nombre}' no se encontró.")
agregar_contacto(agenda, "Munar", "3202394819")
agregar_contacto(agenda, "Natalia", "3202394818")
agregar_contacto(agenda, "Andrea", "3202394810")

print("\nAgenda actual:", agenda)

# Buscamos un contacto existente
buscar_contacto(agenda, "Munar")

# Buscamos un contacto que no existe
buscar_contacto(agenda, "Ana")

# Eliminamos un contacto
eliminar_contacto(agenda, "Natalia")

print("\nAgenda después de eliminar a Natalia:", agenda)

# Intentamos eliminar un contacto que no existe
eliminar_contacto(agenda, "Carlos")        