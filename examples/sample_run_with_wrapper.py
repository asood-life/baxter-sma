import gym
import baxter_env
import pybullet as p
import matplotlib.pyplot as plt
import pybullet_data
import numpy as np
import cv2
import time

# Custom observation wrapper to process and scale observations
class ObsWrapper(gym.ObservationWrapper):
    def __init__(self, env):
        super(ObsWrapper, self).__init__(env)
        # Define the shape and range of the observation space
        self.observation_space = gym.spaces.Box(low=-1, high=1, shape=(128, 128, 4))

    def observation(self, obs):
        # Take the image from the state dictionary and scale it to range [-1, 1]
        img = obs['eye_view'] / 255.0
        # Take the depth map from the state dictionary and scale it (max depth is 10 and min is 0)
        depth = obs['depth'].reshape(img.shape[0], img.shape[0], 1) / 10.0
        # Concatenate image and depth map along the last axis
        obs = np.concatenate([img, depth], axis=-1)
        # Clip the observation values to the range [-1, 1]
        obs = np.clip(obs, -1, 1)
        return obs.reshape((128, 128, 4))

# Custom action wrapper to process and scale actions
class ActWrapper(gym.ActionWrapper):
    def __init__(self, env, action_verbose=100):
        self.action_steps = 0
        self.action_verbose = action_verbose
        super(ActWrapper, self).__init__(env)
        # Define the shape and range of the action space
        self.action_space = gym.spaces.Box(-1, 1, (6,))

    def action(self, act):
        # Scale actions from range [-1, 1] to [0, 20]
        act = (act + 1) * 10
        act = np.clip(act, 0, 20)
        # Print action details periodically based on action_verbose
        if self.action_steps % self.action_verbose == 0:
            print(f"actions took in action_step {self.action_steps} are: {act}")
        self.action_steps += 1
        return act

# Function to create and wrap the environment
def make_env():
    env = gym.make('baxter_env-v0')
    env = ObsWrapper(env)
    env = ActWrapper(env)
    return env

if __name__ == "__main__":
    env = make_env()  # Create the environment
    s = env.reset()  # Reset the environment to get the initial state
    num_step = 0
    while True:
        action = env.sample_action()  # Sample a random action
        next_state, r, done, info = env.step(action)  # Take a step in the environment
        s = next_state  # Update the state
        # Print step details
        print(f"Completed Step: {num_step}")
        print("Reward: ", r)
        print("Done: ", done)
        print("Info: ", info)
        num_step += 1  # Increment the step counter
        if done:  # If the episode is done, break the loop
            break
