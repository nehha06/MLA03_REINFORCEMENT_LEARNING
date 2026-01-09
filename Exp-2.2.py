import random

returns = []

for _ in range(100):
    time = random.randint(5, 20)
    fuel = random.randint(3, 10)
    reward = -(time + fuel)
    returns.append(reward)

print("Average Return:", sum(returns) / len(returns))
