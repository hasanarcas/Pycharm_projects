from snake import SnakeEnv
from stable_baselines3 import PPO
import gym

models_dir = "models/1645030896"

env = SnakeEnv()
env.reset()

model_path = f"{models_dir}/160000.zip"
model = PPO.load(model_path, env = env)

episodes = 10

for ep in range(episodes):
    obs = env.reset()
    done = False
    while not done:
        action, _states = model.predict(obs)
        obs, reward, done, info =  env.step(action)
        print(reward)

env.close()