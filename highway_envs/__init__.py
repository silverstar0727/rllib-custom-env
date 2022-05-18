from gym.envs.registration import register

register(
    id='highway-fast-v2',
    entry_point='highway_envs.v1:HighwayEnv'
)