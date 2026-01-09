import random

grid = [[0]*5 for _ in range(5)]
dirt = [(1,1),(2,3),(4,2)]
obstacles = [(3,3)]

for d in dirt:
    grid[d[0]][d[1]] = 1
for o in obstacles:
    grid[o[0]][o[1]] = -1

x, y = 0, 0
reward = 0

for _ in range(20):
    move = random.choice(['up','down','left','right'])

    if move == 'up' and x > 0: x -= 1
    if move == 'down' and x < 4: x += 1
    if move == 'left' and y > 0: y -= 1
    if move == 'right' and y < 4: y += 1

    reward += grid[x][y]
    print("Position:", (x,y), "Reward:", reward)
