import random

# Definir la semilla
#1160
seed = float(input("introduce un numero: "))
random.seed(seed)

# Parámetros del sistema
casillas = 30  # Número de casillas posibles
puestos = 12  # Número de posiciones por carrete
simbolos = ['A', 'B', 'C']  # Tres símbolos posibles

# Función para generar las combinaciones de símbolos
def generar_combinacion():
    combinacion = []
    for _ in range(puestos):
        combinacion.append(random.choice(simbolos))
    return combinacion

# Generar una secuencia de combinaciones
combinaciones = [generar_combinacion() for _ in range(casillas)]

# Mostrar las combinaciones generadas
for idx, combinacion in enumerate(combinaciones):
    print(f"Casilla {idx + 1}: {combinacion}")
