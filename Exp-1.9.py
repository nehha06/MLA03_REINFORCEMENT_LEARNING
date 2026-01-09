import random

returns = []

for _ in range(100):
    episode_reward = random.randint(1,10)
    returns.append(episode_reward)

print("Estimated Value:", sum(returns)/len(returns))
