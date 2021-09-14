import nashpy as nash

import numpy as np
import random

A = np.array([[4, 1], [5, 2]])

B = np.array([[4, 5], [1, 2]])

prisoners_dilemma = nash.Game(A, B)

print(prisoners_dilemma)
for eq in prisoners_dilemma.support_enumeration():
    print(eq)

for i in range(0,3):
    playerA = input("ENTER C OR D OR R\r\n")
    playerB = input("ENTER C OR D OR R\r\n")
    if playerA == "C":
        inputA = [1,0]
    elif playerA == "R":
        if random.randint(1,100) < 50:
            inputA = [1,0]
        else:
            inputA = [0,1]
    else:
        inputA = [0,1]
    if playerB == "C":
        inputB = [1,0]
    elif playerB == "R":
        if random.randint(1,100) < 50:
            inputB = [1,0]
        else:
            inputB = [0,1]
    else:
        inputB = [0,1]

    result = prisoners_dilemma[inputA,inputB]
    print(result)
