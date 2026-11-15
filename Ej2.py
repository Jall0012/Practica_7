import numpy as np

alternativas = 4
criterios = 4
jugadores = np.array([
    [0.3, 10000, 12, 4],
    [0.35, 12000, 12, 2],
    [0.5, 6000, 2, 4],
    [0.2, 20000, 15, 4]
], dtype=float)

matrizpesos = matriz = np.array([
    [1,   3,   6,   8],
    [1/3, 1,   2,   3],
    [1/6, 1/2, 1,   4],
    [1/8, 1/3, 1/4, 1]
], dtype=float)

autovalores, autovectores = np.linalg.eig(matriz)

autovectores = autovectores.real
autovalores = autovalores.real

psoicionmax = np.argmax(autovalores)

vectorfinal = autovectores[:,psoicionmax]

sumatorio = sum(vectorfinal)

if sumatorio != 0:
    sol = vectorfinal/sumatorio
else:
    sol = vectorfinal

print("Pesos:")
print(sol)
print("\n")
pesos = np.array(sol)

benef = np.array(["C", "C", "B", "B"])

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


distanciasposideal = np.sqrt(np.sum((matrizponderadaIdeal - idealactionIdeal) ** 2, axis=1))
distanciasnegideal = np.sqrt(np.sum((matrizponderadaIdeal - antidealactionIdeal) ** 2, axis=1))

distanciasposnorm = np.sqrt(np.sum((matriznormalizadoNorma - idealactionNorma) ** 2, axis=1))
distanciasnegnorm = np.sqrt(np.sum((matriznormalizadoNorma - antidealactionNorma) ** 2, axis=1))

distanciasrelativasideal = distanciasnegideal / (distanciasposideal + distanciasnegideal)
distanciasrelativasnorm = distanciasnegnorm / (distanciasposnorm + distanciasnegnorm)

print("--- Puntuaciones (Normalización Ideal) ---")
print(distanciasrelativasideal)

print("\n--- Puntuaciones (Normalización Vectorial / Norma) ---")
print(distanciasrelativasnorm)