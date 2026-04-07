#Primer punto taller
#Ivan Daniel Obregon Cuellar 
#05/04/2026
#Ingenieria en contexto
def calcular_promedio(notas):
    suma_total = 0
    for nota in notas:
        suma_total = suma_total + nota
    if len(notas) > 0:
        promedio = suma_total / len(notas)
    else:
        promedio = 0 
    return promedio
def calcular_nota_mas_alta(notas):
    if not notas:
        return None 
    
    nota_mas_alta = notas[0] 
    for nota in notas:
        if nota > nota_mas_alta:
            nota_mas_alta = nota 
    return nota_mas_alta
def calcular_nota_mas_baja(notas):
    if not notas:
        return None #
    
    nota_mas_baja = notas[0] 
    for nota in notas:
        if nota < nota_mas_baja:
            nota_mas_baja = nota 
    return nota_mas_baja
mis_notas = [4.5, 3.2, 2.8, 2.5, 4.8, 2.4, 1.0]
mi_promedio = calcular_promedio(mis_notas)
print(f"El promedio de las notas es: {mi_promedio:.2f}")
mi_nota_mas_alta = calcular_nota_mas_alta(mis_notas)
print(f"La nota más alta es: {mi_nota_mas_alta}")
mi_nota_mas_baja = calcular_nota_mas_baja(mis_notas)
print(f"La nota más baja es: {mi_nota_mas_baja}")

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
print("\nProbando con una lista vacía de estudiantes:")
print(filtrar_aprobados([]))
estudiantes_que_aprobaron = filtrar_aprobados(lista_estudiantes)

print("Lista original de estudiantes:", lista_estudiantes)
print("Estudiantes aprobados:", estudiantes_que_aprobaron)