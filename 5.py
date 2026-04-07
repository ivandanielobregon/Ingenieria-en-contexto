def contar_frecuencia_palabras(lista_palabras):
    frecuencia = {} 
    for palabra in lista_palabras:
        if palabra in frecuencia:
            frecuencia[palabra] += 1
        else:
            frecuencia[palabra] = 1
    return frecuencia
texto_ejemplo = [
    "manzana", "banana", "manzana", "pera", "banana", "manzana", "uva", "pera"
]
frecuencia_palabras = contar_frecuencia_palabras(texto_ejemplo)
print("Lista de palabras de ejemplo:", texto_ejemplo)
print("\nFrecuencia de las palabras:", frecuencia_palabras)