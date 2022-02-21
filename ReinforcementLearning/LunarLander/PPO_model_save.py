import gym
from stable_baselines3 import PPO
import os

models_dir = "models/PPO"
log_dir = "logs/"

if not os.path.exists(models_dir):
    os.makedirs(models_dir)
if not os.path.exists(log_dir):
    os.makedirs(log_dir)

env = gym.make("LunarLander-v2")
env.reset()

model = PPO("MlpPolicy", env , verbose=1, tensorboard_log=log_dir, device= "cuda")

TIMESTEPS = 20000
i = 1
while True:
    model.learn(total_timesteps=TIMESTEPS, reset_num_timesteps=False, tb_log_name="PPO")
    model.save(f"{models_dir}/{TIMESTEPS*i}")
    i += 1

env.close()