import gymnasium as gym
from gymnasium.envs.registration import register

# Register your custom environment
register(
    id="Factorio-open_play-v0",
    entry_point="fle.env.gym_env.environment:FactorioGymEnv",
)

def main():
    env_id = "Factorio-open_play-v0"

    try:
        env = gym.make(env_id)
        obs, info = env.reset()
        print("Initial observation:", obs)

        for step in range(5):
            action = env.action_space.sample()  # Replace with agent logic if needed
            obs, reward, terminated, truncated, info = env.step(action)
            print(f"Step {step + 1}: reward={reward}, terminated={terminated}, truncated={truncated}")

            if terminated or truncated:
                obs, info = env.reset()

    except Exception as e:
        print(f"Environment test failed: {e}")

if __name__ == "__main__":
    main()