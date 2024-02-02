# script for checking CompilerGym installation
import gym
import compiler_gym

# env = compiler_gym.make("llvm-v0")
env = gym.make("llvm-autophase-ic-v0")

print(env)

# help(env.step)
# print(env.)

env.reset()

print(env)