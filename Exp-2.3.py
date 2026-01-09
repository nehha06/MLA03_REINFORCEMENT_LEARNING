import numpy as np

V = np.zeros(5)
alpha = 0.1
gamma = 0.9

for _ in range(20):
    for s in range(4):
        V[s] += alpha * (1 + gamma * V[s+1] - V[s])

print("State Values:", V)
