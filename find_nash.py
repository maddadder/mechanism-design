import nashpy as nash

import numpy as np
import random

'''
_i, _j represent opponents actions 
'''
def find_best_response_given_i_j(A, B, _i, _j):
    max_utility = 0
    i = 0
    selected_i = 0
    selected_j = 0
    for i in range(len(B)):
        for j in range(len(B[i])):
            if (i == _i and j == _j) or (_i == None and _j == None):
                current_utility = B[i][j]
                if current_utility > max_utility:
                    max_utility = current_utility
                    selected_i = i
                    selected_j = j
    return max_utility, selected_i, selected_j

def find_nash(A, B):
    index = []
    scores = []
    print('row_player\r\n',A)
    print('column_player\r\n',B)
    global_best_response, __i, __j = find_best_response_given_i_j(A, B, None, None)
    i = 0
    for i in range(len(A)):
        for j in range(len(A[i])):
            max_utility, _i, _j = find_best_response_given_i_j(A, B, i, j)
            if max_utility >= A[i][j]:
                max_utility = A[i][j]
                index = np.array([i,j]), np.array([_i,_j])
                scores = np.array([A[i][j], max_utility])
    return index, scores, max_utility

# battle of the sexes
A = np.array([[2, 0, -1], [0, 1, -1], [0, 0, -2]])
B = np.array([[1, 0, 0], [0, 2, 0], [-1, -1, -2]])

# prisoner's delimma
A = np.array([[3, 0], [5, 1]])
B = np.array([[3, 5], [0, 1]])

# For the Pigs Game
A = np.array([[4, 6], [2, 0]])
B = np.array([[2, -1], [3, 0]])


index, scores, max_utility = find_nash(A,B)
print(index, scores, max_utility)
