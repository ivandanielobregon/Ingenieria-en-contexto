reporte= []
def convertir_nota_a_letra(nota_numerica):
    if not (0.1 <= nota_numerica <= 5.0):
        return "Error: La nota debe estar entre 0.1 y 5.0"
    elif 4.5 <= nota_numerica <= 5.0:
        return 'A'
    elif 3.5 <= nota_numerica < 4.5:
        return 'B'
    elif 2.5 <= nota_numerica < 3.5:
        return 'C'
    elif 1.5 <= nota_numerica < 2.5:
        return 'D'
    elif 0.1 <= nota_numerica < 1.5:
        return 'F'
    else:
        return "Nota Inválida (rango inesperado)"
def generar_reporte_estudiantes(lista_estudiantes):
    for nombre, nota_numerica in lista_estudiantes:
        nota_letra = convertir_nota_a_letra(nota_numerica)
        reporte.append((nombre, nota_numerica, nota_letra))
    return reporte
estudiantes_con_notas = [
    ("Sofía", 4.8),
    ("Carlos", 3.7),
    ("Ana", 2.9),
    ("Luis", 2.2),
    ("María", 1.0),
    ("Pedro", 5.0),
    ("Elena", 3.4),
    ("Juan", 0.0), 
    ("Laura", 4.5) 
]    
reporte_final = generar_reporte_estudiantes(estudiantes_con_notas)

print("Reporte de Estudiantes:")
for estudiante in reporte_final:
    print(f"Nombre: {estudiante[0]}, Nota Numérica: {estudiante[1]}, Nota de Letra: {estudiante[2]}")