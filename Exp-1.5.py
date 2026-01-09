import numpy as np

V = np.zeros(5)

for _ in range(10):
    V = np.maximum(V + 1, V)

print("Optimal Values:", V)
