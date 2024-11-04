import simpy

def heat_exchange(env):
    while True:
        print(f"Heat exchange happening at {env.now}")
        yield env.timeout(1)  # Simulate the process happening every second

env = simpy.Environment()
env.process(heat_exchange(env))
env.run(until=10)
