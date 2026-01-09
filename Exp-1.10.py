import random

policy = 0.5

for _ in range(10):
    reward = random.random()
    policy += 0.1 * reward

print("Optimized Policy:", policy)
