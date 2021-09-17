import numpy as np

def f1(x):
    return x * 1 + ((1-x)*(1/2))
def f2(x):
    return x*(3/2)

steps = 101
min = 0
max = 1
solution = 0
for xi in np.linspace(min,max,steps):
    _f1 = f1(xi)
    _f2 = f2(xi)
    if _f1 <= _f2:
        solution = xi
        break

print('solution:',solution," found")