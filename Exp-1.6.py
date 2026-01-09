import random

ads = [0,0,0]
clicks = [0,0,0]

for _ in range(100):
    ad = random.randint(0,2)
    reward = random.choice([0,1])
    clicks[ad] += reward

print("Ad Clicks:", clicks)
