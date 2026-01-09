import gym

env = gym.make("CartPole-v1")
state = env.reset()

for _ in range(10):
    action = env.action_space.sample()
    state, reward, done, _ = env.step(action)
    if done:
        break

print("CartPole executed successfully")
