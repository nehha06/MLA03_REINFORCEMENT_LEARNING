import random

Q = [0]*9
alpha = 0.1

for _ in range(50):
    move = random.randint(0,8)
    reward = random.choice([1,-1])
    Q[move] += alpha * (reward - Q[move])

print("Learned Q Values:", Q)
