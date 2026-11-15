from itertools import count

import numpy as np

Aclasificar = np.array([
    [18, 110, 8, 5],
    [28, 165, 10, 9],
    [35, 130, 14, 6],
    [12, 210, 11, 8],
    [38, 180, 15, 10],
    [24, 105, 6, 12],
    [58, 290, 24, 18],
    [72, 380, 30, 22],
    [84, 310, 32, 24],
    [65, 450, 26, 29],
    [95, 420, 42, 26],
    [76, 510, 36, 31],
    [102, 480, 39, 35],
    [88, 540, 43, 30],
    [135, 720, 61, 49],
    [160, 650, 68, 55],
    [145, 810, 72, 58],
    [178, 880, 82, 63],
    [155, 760, 75, 67],
    [190, 930, 90, 74]
    ]
)

alternativas = 24
criterios = 4
matr = np.array([
    [0, 0, 0, 0],
    [45, 220, 18, 12],
    [115, 600, 55, 42],
    [200, 1000, 100, 80],
], dtype=float)

matr = np.vstack((Aclasificar,matr))

nombreAlternativa = ""
nombregrupo = ["Baja","Media","Alta"]
pesos = np.array([0.35, 0.25, 0.20, 0.20])
benef = np.array(["B", "B", "B", "B"])

normalizado = np.empty((alternativas,criterios))

for j in range(criterios):
    columna = matr[:, j]
    mini = np.min(columna)
    maxi = np.max(columna)
    if benef[j] == "B":
        normalizado[:, j] = (columna - mini) / (maxi - mini)
    else:
        normalizado[:, j] = (maxi - columna) / (maxi - mini)


matrizponderada = normalizado * pesos

idealactionIdeal = np.empty(criterios)
antidealactionIdeal = np.empty(criterios)

for j in range(criterios):
    if benef[j] == "B":
        idealactionIdeal[j] = np.max(matrizponderada[:, j])
        antidealactionIdeal[j] = np.min(matrizponderada[:, j])
    else:
        antidealactionIdeal[j] = np.max(matrizponderada[:, j])
        idealactionIdeal[j] = np.min(matrizponderada[:, j])

distanciasposideal = np.sqrt(np.sum((matrizponderada - idealactionIdeal) ** 2, axis=1))
distanciasnegideal = np.sqrt(np.sum((matrizponderada - antidealactionIdeal) ** 2, axis=1))


distanciasrelativasideal = distanciasnegideal / (distanciasposideal + distanciasnegideal)

print(f"Limite 1: {distanciasrelativasideal[len(Aclasificar) + 1]}")
print(f"Limite 2: {distanciasrelativasideal[len(Aclasificar) + 2]}")
for i in range(len(Aclasificar)):
    if distanciasrelativasideal[i] < distanciasrelativasideal[len(Aclasificar) + 1]:
        print(f"La Alternativa {i} esta dentro del grupo {nombregrupo[0]} con una puntuacion de {distanciasrelativasideal[i]}")
    elif distanciasrelativasideal[i] < distanciasrelativasideal[len(Aclasificar) + 2]:
        print(f"La Alternativa {i} esta dentro del grupo {nombregrupo[1]} con una puntuacion de {distanciasrelativasideal[i]}")
    else:
        print(f"La Alternativa {i} esta dentro del grupo {nombregrupo[2]} con una puntuacion de {distanciasrelativasideal[i]}")