#Segundo punto
def filtrar_aprobados(estudiantes):
    estudiantes_aprobados = [] 
    for nombre, nota in estudiantes: 
        if nota >= 3.0: 
            estudiantes_aprobados.append((nombre, nota)) 
    return estudiantes_aprobados
lista_estudiantes = [
    ("Ana", 4.5),
    ("Luis", 2.8),
    ("María", 3.0),
    ("Carlos", 1.5),
    ("Sofía", 4.0)
]
estudiantes_que_aprobaron = filtrar_aprobados(lista_estudiantes)

print("Lista original de estudiantes:", lista_estudiantes)
print("Estudiantes aprobados:", estudiantes_que_aprobaron)