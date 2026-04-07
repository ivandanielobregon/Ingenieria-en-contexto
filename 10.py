def registrar_votos(lista_votos, candidatos_validos):
    conteo_votos = {candidato: 0 for candidato in candidatos_validos} 
    votos_invalidos = 0
    total_votos_emitidos = len(lista_votos)

    print(f"Total de votos emitidos: {total_votos_emitidos}")

    for voto in lista_votos:
        if voto in candidatos_validos:
            conteo_votos[voto] += 1
        else:
            votos_invalidos += 1
            print(f"Voto inválido detectado: '{voto}'")
    return conteo_votos, votos_invalidos

def determinar_ganador(conteo_votos, votos_invalidos):
    total_votos_validos = sum(conteo_votos.values())

    if total_votos_validos == 0 and votos_invalidos == 0:
        print("No se emitieron votos válidos ni inválidos.")
        return None, None
    elif total_votos_validos == 0 and votos_invalidos > 0:
        print(f"No hay votos válidos. Total de votos inválidos: {votos_invalidos}.")
        return None, None

    print(f"\nTotal de votos válidos: {total_votos_validos}")
    if votos_invalidos > 0:
        print(f"Votos inválidos: {votos_invalidos}")

    porcentajes = {}
    for candidato, votos in conteo_votos.items():
        porcentaje = (votos / total_votos_validos) * 100 if total_votos_validos > 0 else 0
        porcentajes[candidato] = porcentaje
        print(f"{candidato}: {votos} votos ({porcentaje:.2f}%)")

    if not conteo_votos:
        return "No hay candidatos válidos con votos.", None

    ganador = max(conteo_votos, key=conteo_votos.get)
    porcentaje_ganador = porcentajes[ganador]

    votos_ganador = conteo_votos[ganador]
    otros_candidatos_con_mismos_votos = [c for c, v in conteo_votos.items() if v == votos_ganador and c != ganador]

    if otros_candidatos_con_mismos_votos:
        empatados = [ganador] + otros_candidatos_con_mismos_votos
        print(f"\n¡EMPATE! Los candidatos empatados son: {', '.join(empatados)} con {votos_ganador} votos ({porcentaje_ganador:.2f}% cada uno).")
        return empatados, porcentaje_ganador
    else:
        print(f"\nEl ganador es: {ganador} con {votos_ganador} votos ({porcentaje_ganador:.2f}%). ¡Felicidades!")
        return ganador, porcentaje_ganador
candidatos = ["Juan", "Maria", "Pedro"]

votos_emitidos = [
    "Juan", "Maria", "Juan", "Pedro", "Maria", "Juan",
    "Juan", "Carlos", "Maria", "Pedro", "Maria", "Monica",
    "Pedro", "Juan", "Maria", "Juan", "Pedro", "Juan"
]

print("--- Resultados de la Elección ---")
conteo, invalidos = registrar_votos(votos_emitidos, candidatos)

ganador_eleccion, porcentaje_ganador_eleccion = determinar_ganador(conteo, invalidos)

print("\n--- Escenario de Empate ---")

votos_empate = ["Juan", "Maria", "Juan", "Maria"]
conteo_empate, invalidos_empate = registrar_votos(votos_empate, candidatos)
determinar_ganador(conteo_empate, invalidos_empate)

print("\n--- Escenario sin votos válidos ---")

votos_solo_invalidos = ["Carlos", "Monica"]
conteo_solo_invalidos, invalidos_solo_invalidos = registrar_votos(votos_solo_invalidos, candidatos)
determinar_ganador(conteo_solo_invalidos, invalidos_solo_invalidos)