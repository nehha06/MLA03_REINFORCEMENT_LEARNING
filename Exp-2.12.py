import random

V = 0
for _ in range(20):
    reward = random.randint(-5,10)
    V += 0.1 * (reward - V)

print("Portfolio Value:", V)
