temperaturas_semanales = {}
def registrar_temperaturas(temperaturas_dict, ciudad, lista_de_temps):
    temperaturas_dict[ciudad] = lista_de_temps 
    print(f"Temperaturas de '{ciudad}' registradas: {lista_de_temps}")
def temperatura_mas_alta_ciudad(temperaturas_dict, ciudad):
    if ciudad in temperaturas_dict and temperaturas_dict[ciudad]:
        return max(temperaturas_dict[ciudad]) 
    else:
        return "No hay datos de temperatura para esta ciudad o la lista está vacía."
def temperatura_mas_baja_ciudad(temperaturas_dict, ciudad):
    if ciudad in temperaturas_dict and temperaturas_dict[ciudad]:
        return min(temperaturas_dict[ciudad]) 
    else:
        return "No hay datos de temperatura para esta ciudad o la lista está vacía."
def temperatura_mas_alta_general(temperaturas_dict):
    todas_las_temps = []
    for ciudad in temperaturas_dict:
        todas_las_temps.extend(temperaturas_dict[ciudad]) 
    if todas_las_temps:
        return max(todas_las_temps)
    else:
        return "No hay temperaturas registradas en ninguna ciudad."
def temperatura_mas_baja_general(temperaturas_dict):
    todas_las_temps = []
    for ciudad in temperaturas_dict:
        todas_las_temps.extend(temperaturas_dict[ciudad]) 
    if todas_las_temps:
        return min(todas_las_temps)
    else:
        return "No hay temperaturas registradas en ninguna ciudad."
    
registrar_temperaturas(temperaturas_semanales, "Madrid", [15, 18, 20, 22, 19, 17, 16])
registrar_temperaturas(temperaturas_semanales, "Londres", [10, 12, 11, 14, 13, 10, 9])

print("\nDiccionario de temperaturas actual:", temperaturas_semanales)

print(f"\nTemperatura más alta en Madrid: {temperatura_mas_alta_ciudad(temperaturas_semanales, 'Madrid')}°C")
print(f"Temperatura más baja en Madrid: {temperatura_mas_baja_ciudad(temperaturas_semanales, 'Madrid')}°C")

print(f"Temperatura más alta en Londres: {temperatura_mas_alta_ciudad(temperaturas_semanales, 'Londres')}°C")
print(f"Temperatura más baja en Londres: {temperatura_mas_baja_ciudad(temperaturas_semanales, 'Londres')}°C")

print(f"\nTemperatura más alta de la semana (general): {temperatura_mas_alta_general(temperaturas_semanales)}°C")
print(f"Temperatura más baja de la semana (general): {temperatura_mas_baja_general(temperaturas_semanales)}°C")      