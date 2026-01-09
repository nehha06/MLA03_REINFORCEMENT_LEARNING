import numpy as np

V = np.zeros(5)

for _ in range(10):
    for s in range(5):
        V[s] = 1 + 0.9 * V[s]

print("State Values:", V)
