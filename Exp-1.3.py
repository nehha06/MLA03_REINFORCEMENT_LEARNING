import random

prices = [10,20,30]
values = [0,0,0]
counts = [0,0,0]
epsilon = 0.1

for _ in range(100):
    if random.random() < epsilon:
        arm = random.randint(0,2)
    else:
        arm = values.index(max(values))

    reward = random.randint(0, prices[arm])
    counts[arm] += 1
    values[arm] += (reward - values[arm]) / counts[arm]

print("Estimated Values:", values)
