# Peyman Miyandashti 250161
# Sistema de votación para elección de cargos con manejo de empates
# inicio
def Algoritmo_votar():
    """
    Sistema de votación para elegir:
    - Jefe de Grupo (1er lugar)
    - Tesorero (2do lugar)
    - Reconocimiento al 3er lugar
    Con manejo de empates y opción de revotación
    """
    while True:
        # Inicialización de variables
        #leer
        candidatos = {'Hugo': 0, 'Paco': 0, 'Luis': 0}

        total_alumnos = 15
        
        # Encabezado del sistema

        print("="*60)
        print("★ SISTEMA DE VOTACIÓN ESCOLAR ★".center(60))
        print("="*60)
        print("\nCANDIDATOS DISPONIBLES:")
        print("1. Hugo - Candidato a Jefe de Grupo")
        print("2. Paco - Candidato a Tesorero")
        print("3. Luis - Candidato")
        print("="*60)
        print("Cada alumno debe votar por 1 candidato (1-3)\n")

        # Proceso de votación

        for alumno in range(1, total_alumnos + 1):
            while True:
                try:
                    voto = int(input(f"Voto #{alumno}: Ingrese su elección (1-3): "))
                    if 1 <= voto <= 3:
                        if voto == 1:
                            candidatos['Hugo'] += 1
                            print("Voto registrado para Hugo")
                        elif voto == 2:
                            candidatos['Paco'] += 1
                            print("Voto registrado para Paco")
                        else:
                            candidatos['Luis'] += 1
                            print("Voto registrado para Luis")
                        break
                    print("Error: Ingrese un número entre 1 y 3")
                except ValueError:
                    print("Error: Debe ingresar solo números")
            print("-"*40)

        # Verificar empate
        valores = list(candidatos.values())
        if all(v == valores[0] for v in valores):
            print("\n" + "!"*60)
            print("¡EMPATE DETECTADO!".center(60))
            print("Todos los candidatos tienen", valores[0], "votos")
            print("Se reiniciará la votación...")
            print("!"*60 + "\n")
            continue  # Reiniciar el proceso de votación

        # Procesamiento de resultados
        resultados = sorted(candidatos.items(), key=lambda x: x[1], reverse=True)
        
        # Cálculo de porcentajes
        porcentajes = {
            nombre: (votos / total_alumnos) * 100 
            for nombre, votos in resultados
        }

        # Presentación de resultados
        print("\n" + "="*60)
        print("★ RESULTADOS FINALES ★".center(60))
        print("="*60)
        
        # Jefe de Grupo (1er lugar)
        print("\n" + "★"*20 + " JEFE DE GRUPO " + "★"*20)
        print(f"\n🏆 GANADOR: {resultados[0][0].upper()} 🏆")
        print(f"📊 Votos: {resultados[0][1]} ({porcentajes[resultados[0][0]]:.1f}%)")
        print("\n¡FELICIDADES POR GANAR EL PRIMER LUGAR!")
        print("-"*60)
        
        # Tesorero (2do lugar)
        print("\n" + "✦"*15 + " TESORERO DEL GRUPO " + "✦"*15)
        print(f"\n🎖️ SEGUNDO LUGAR: {resultados[1][0].upper()}")
        print(f"📊 Votos: {resultados[1][1]} ({porcentajes[resultados[1][0]]:.1f}%)")
        print("\n¡BUEN TRABAJO COMO TESORERO!")
        print("-"*60)
        
        # Reconocimiento (3er lugar)
        print("\n" + "♡"*10 + " RECONOCIMIENTO POR PARTICIPACIÓN " + "♡"*10)
        print(f"\n🤝 TERCER LUGAR: {resultados[2][0]}")
        print(f"📊 Votos: {resultados[2][1]} ({porcentajes[resultados[2][0]]:.1f}%)")
        print("\n¡GRACIAS POR TU PARTICIPACIÓN Y ESFUERZO!")
        print("="*60)
        
        break  # Salir del bucle si no hay empate

# Ejecutar el programa
Algoritmo_votar()