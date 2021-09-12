import nashpy as nash

import numpy as np
import random

def find_best_response(A,B):
    
    index = []
    scores = []
    #print('row_player\r\n',A)
    #print('column_player\r\n',B)
    i = 0
    max_utility = 0
    for a, b in zip(A,B):
        for j in range(len(a)):
            #print('current_j',j)
            print(a[j],b[j])
            current_utility = a[j]
            #print('current_utility',current_utility)
            if current_utility > max_utility:
                max_utility = current_utility
                index = np.array([i, j])
                #print('index',i,j)
                scores = np.array([a[j], b[j]])
        i += 1
    return index, scores, max_utility

# battle of the sexes
A = np.array([[2, 0, -1], [0, 1, -1], [0, 0, -2]])
B = np.array([[1, 0, 0], [0, 2, 0], [-1, -1, -2]])

# prisoner's delimma
A = np.array([[3, 0], [5, 1]])
B = np.array([[3, 5], [0, 1]])

# Cournot duopoly
# A = np.array([[3, 0], [5, 1]])
# B = np.array([[3, 5], [0, 1]])

index, scores, max_utility = find_best_response(A,B)
print(index, scores, max_utility)
