import random

weights = random.random()

for _ in range(10):
    reward = random.randint(1, 10)
    weights += 0.01 * reward

print("Learned Weight:", weights)
