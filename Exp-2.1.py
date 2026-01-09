import numpy as np

states = 2
actions = 2
V = np.zeros(states)
policy = np.zeros(states, dtype=int)
gamma = 0.9

for _ in range(10):
    # Policy Evaluation
    for s in range(states):
        V[s] = -1 + gamma * V[s]

    # Policy Improvement
    for s in range(states):
        policy[s] = np.argmax([V[s], V[s] + 1])

print("Optimal Policy:", policy)
print("Value Function:", V)
