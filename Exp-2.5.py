import random

Q = [[0]*4 for _ in range(5)]
alpha, gamma = 0.1, 0.9

for _ in range(100):
    s = random.randint(0, 4)
    a = random.randint(0, 3)
    r = random.choice([1, -1])
    s2 = min(4, s+1)

    Q[s][a] += alpha * (r + gamma * max(Q[s2]) - Q[s][a])

print("Q Table:", Q)
