#https://stackoverflow.com/questions/47759577/creating-a-mixture-of-probability-distributions-for-sampling

import numpy as np
import matplotlib.pyplot as plt

distributions = [
    {"type": np.random.normal, "kwargs": {"loc": 4, "scale": 1}}, # A goods (our produts average at loc per item)
    {"type": np.random.normal, "kwargs": {"loc": 5, "scale": 1}}, # B buyers (everyone has about loc dollars in their pocket)
]

sample_size = 10000

num_distr = len(distributions)
data = np.zeros((sample_size, num_distr))
for idx, distr in enumerate(distributions):
    data[:, idx] = distr["type"](size=(sample_size,), **distr["kwargs"])
A = data[:, 0]
#plt.hist(A, bins=100, density=True)
#plt.show()
B = data[:, 1]
#plt.hist(B, bins=100, density=True)
#plt.show()
S = [xv if c else 0
 for c, xv, yv in zip(A < B, A, B)] # S affordable goods
plt.hist(S, bins=100, density=True)
plt.show()
