import numpy as np

def f1(x):
    return x * 1 + ((1-x)*(1/2))
def f2(x):
    return x*(3/2)

steps = 1000000
min = 0
max = 10
solution = 0
for xi in np.linspace(min,max,steps):
    _f1 = f1(xi)
    _f2 = f2(xi)
    if round(_f1,5) == round(_f2,5):
        solution = round(xi,1)
        break
if f1(solution) == f2(solution):
    print('solution:',solution," found")