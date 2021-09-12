import nashpy as nash

import numpy as np
import random

def find_best_response(A,B, players_response, players_response_index):
    
    index = []
    scores = []
    #print('row_player\r\n',A)
    #print('column_player\r\n',B)
    max_utility = 0
    for a, b in zip(A,B):
        for i in range(len(a)):
            #print('current_j',i)
            #print(a[i],b[i])
            
            if players_response == a[i] and players_response_index == i:
                #print('players_response',players_response, players_response_index)
                continue
            current_utility = a[i]
            #print('current_utility',current_utility)
            if current_utility > max_utility:
                max_utility = current_utility
                index = i
                #print('index',i,i)
                scores = np.array([a[i], b[i]])
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

index, scores, max_utility = find_best_response(A,B, -1000, -1000)
#print(index, scores, max_utility)

index = []
scores = []
#print('row_player\r\n',A)
#print('column_player\r\n',B)
max_utility = 0
for a, b in zip(A,B):
    for i in range(len(a)):
        index, scores, max_utility = find_best_response(A,B, a[i], i)
        if max_utility >= a[i]:
            max_utility = a[i]
            index = i
            scores = np.array([a[i], max_utility])

print(index, scores, max_utility)
