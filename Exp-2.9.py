import random

memory = []
for _ in range(10):
    memory.append((random.random(), random.randint(1, 5)))

memory.sort(reverse=True)
print("Highest Priority Experience:", memory[0])
