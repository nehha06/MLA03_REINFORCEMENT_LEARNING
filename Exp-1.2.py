import numpy as np

states = 5
V = np.zeros(states)
policy = [0,1,2,3,0]

for _ in range(10):
    for s in range(states):
        V[s] = 1 + 0.9 * V[s]

print("Value Function:", V)
