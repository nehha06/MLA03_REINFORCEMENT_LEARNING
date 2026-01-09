import random

Q1, Q2 = 0.5, 0.5

for _ in range(20):
    reward = random.randint(-5, 10)
    Q1 += 0.1 * reward
    Q2 += 0.1 * reward

print("Final Trading Policy:", (Q1 + Q2) / 2)
