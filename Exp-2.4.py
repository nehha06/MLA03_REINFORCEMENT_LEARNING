import random

Q = [[0]*2 for _ in range(5)]
alpha, gamma = 0.1, 0.9

for _ in range(50):
    s = random.randint(0, 4)
    a = random.randint(0, 1)
    r = random.choice([1, -1])
    s2 = min(4, s+1)
    a2 = random.randint(0, 1)

    Q[s][a] += alpha * (r + gamma * Q[s2][a2] - Q[s][a])

print("Q Table:", Q)
