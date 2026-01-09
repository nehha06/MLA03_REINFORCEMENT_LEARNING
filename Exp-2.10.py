import numpy as np

V = np.zeros((3,3))
for _ in range(10):
    V = 1 + 0.9 * V

print("Value Grid:\n", V)
