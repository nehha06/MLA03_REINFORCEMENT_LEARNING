import random

times = [random.randint(2,10) for _ in range(100)]
print("Average Call Time:", sum(times)/len(times))
