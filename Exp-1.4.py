import numpy as np

policy = np.zeros(4)
value = np.zeros(4)

for _ in range(10):
    value = policy + 1
    policy = value.argmax() * np.ones(4)

print("Optimal Policy:", policy)
