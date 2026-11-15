import numpy as np

alternativas = 4
criterios = 4
jugadores = np.array([
    [65, 191, 12.25, 56],
    [68, 162, 9.43, 64],
    [60, 178, 11.22, 59],
    [75, 203, 11.75, 67],
], dtype=float)

pesos = np.array([0.25, 0.25, 0.20, 0.30])
benef = np.array(["B", "C", "C", "B"])

normalizadoideal = np.empty((alternativas,criterios))
normalizadoNorma = np.empty((alternativas,criterios))

for j in range(alternativas):
    columna = jugadores[:,j]
    if benef[j] == "B":
        normalizadoideal[:, j] = columna / np.max(columna)
    else:
        normalizadoideal[:, j] = np.min(columna) / columna

    norma = np.sqrt(np.sum(columna ** 2))
    normalizadoNorma[:, j] = columna / norma

matrizponderadaIdeal = normalizadoideal * pesos
matriznormalizadoNorma = normalizadoNorma * pesos

print("Matriz normalizada ideal")
print(normalizadoideal)

print("\nMatriz normalizada norma")
print(normalizadoNorma)

print("\nMatriz ponderada ideal")
print(matrizponderadaIdeal)

print("\nMatriz ponderada norma")
print(matriznormalizadoNorma)

idealactionIdeal = np.empty(alternativas)
antidealactionIdeal = np.empty(alternativas)
idealactionNorma = np.empty(alternativas)
antidealactionNorma = np.empty(alternativas)

for j in range(alternativas):
    idealactionIdeal[j] = np.max(matrizponderadaIdeal[:, j])
    antidealactionIdeal[j] = np.min(matrizponderadaIdeal[:, j])

    if benef[j] == "B":
        idealactionNorma[j] = np.max(matriznormalizadoNorma[:, j])
        antidealactionNorma[j] = np.min(matriznormalizadoNorma[:, j])
    else:
        idealactionNorma[j] = np.min(matriznormalizadoNorma[:, j])
        antidealactionNorma[j] = np.max(matriznormalizadoNorma[:, j])

print("Matriz ideal ideal:")
print(idealactionIdeal)

print("\nMatriz antideal ideal:")
print(antidealactionIdeal)

print("\nMatriz ideal norma:")
print(idealactionIdeal)

print("\nMatriz antideal norma:")
print(antidealactionIdeal)

distanciasposideal = np.sqrt(np.sum((matrizponderadaIdeal - idealactionIdeal) ** 2, axis=1))
distanciasnegideal = np.sqrt(np.sum((matrizponderadaIdeal - antidealactionIdeal) ** 2, axis=1))


distanciasposnorm = np.sqrt(np.sum((matriznormalizadoNorma - idealactionNorma) ** 2, axis=1))
distanciasnegnorm = np.sqrt(np.sum((matriznormalizadoNorma - antidealactionNorma) ** 2, axis=1))

print("Matriz distancias ideal positivo normalización ideal:")
print(distanciasposideal)

print("\nMatriz distancias ideal negativo normalización ideal:")
print(distanciasnegideal)

print("\nMatriz distancias ideal positivo normalización norma:")
print(distanciasposnorm)

print("\nMatriz distancias ideal negativo normalización norma:")
print(distanciasnegnorm)

distanciasrelativasideal = distanciasnegideal / (distanciasposideal + distanciasnegideal)
distanciasrelativasnorm = distanciasnegnorm / (distanciasposnorm + distanciasnegnorm)

print("--- Puntuaciones (Normalización Ideal) ---")
print(distanciasrelativasideal)

print("\n--- Puntuaciones (Normalización Vectorial / Norma) ---")
print(distanciasrelativasnorm)