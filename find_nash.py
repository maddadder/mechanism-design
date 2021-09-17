import nashpy as nash

import numpy as np
import random
P1 = 0
P2 = 1

'''
_i, _j represent opponents actions 
'''
def generate_labels(labels_num):
    return list(range(labels_num))

def generate_payout_grid(file):
    payout_grid = []
    for line in file:
        row_array = []
        for payouts in line.split(" "):
            row_array.append([int(payout) for payout in payouts.split(",")])
        payout_grid.append(row_array)
    return payout_grid

def compute_pure_strategies(payout_grid):
    equilibriums = pure_strategy_solutions(payout_grid)
    for s in equilibriums:
        print(s)
    if len(equilibriums) == 0:
        print("No pure strategies")

def pure_strategy_solutions(payout_grid):
    best_payouts = {}
    row_num = len(payout_grid)
    col_num = len(payout_grid[0])
    # column then row
    for c in range(col_num):
        max_payout = max([payout_grid[r][c][P1] for r in range(row_num)])
        for r in range(row_num):
            #print(payout_grid[r][c][P1])
            if payout_grid[r][c][P1] == max_payout:
                best_payouts[(r, c)] = max_payout

    best_payout_labels = []
    # row then column
    for r in range(row_num):
        max_payout = max([payout_grid[r][c][P2] for c in range(col_num)])
        for c in range(col_num):
            #print(payout_grid[r][c][P2])
            if payout_grid[r][c][P2] == max_payout:
                if (r, c) in best_payouts:
                    best_payout_labels.append({(r, c),(best_payouts[(r, c)])})
    return best_payout_labels

fileName = "games/prisonersDelimma.txt"
#fileName = "games/PigsGame.txt"
#fileName = "games/HawkDoveGame.txt"
file = open(fileName, "r")
payout_grid = generate_payout_grid(file)
row_labels = generate_labels(len(payout_grid))
col_labels = generate_labels(len(payout_grid[0]))
file.close()

compute_pure_strategies(payout_grid)

