import nashpy as nash

import numpy as np
import random

# battle of the sexes
A = np.array([[2, 0, -1], [0, 1, -1], [0, 0, -2]])
B = np.array([[1, 0, 0], [0, 2, 0], [-1, -1, -2]])

# prisoner's delimma
#A = np.array([[3, 0], [5, 1]])
#B = np.array([[3, 5], [0, 1]])

# Cournot duopoly
A = np.array([[3, 0], [5, 1]])
B = np.array([[3, 5], [0, 1]])

game = nash.Game(A,B)


print(game)
final = []
for eq in game.support_enumeration():
    for y in eq:
        final.append(y)

print(final)
score = game[final[0],final[1]]
print('score',score)
is_best_response = game.is_best_response(final[0],final[1])
print(is_best_response)
print(game.is_best_response(np.array([1, 0]),np.array([1, 0])))