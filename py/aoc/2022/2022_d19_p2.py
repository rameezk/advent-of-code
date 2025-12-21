from aoc.helper import AOC
import re


@AOC.puzzle(2022, 19, 2)
def solve():
    data = AOC.get_data().strip().splitlines()

#     data = """Blueprint 1: Each ore robot costs 4 ore. Each clay robot costs 2 ore. Each obsidian robot costs 3 ore and 14 clay. Each geode robot costs 2 ore and 7 obsidian.
# Blueprint 2: Each ore robot costs 2 ore. Each clay robot costs 3 ore. Each obsidian robot costs 3 ore and 8 clay. Each geode robot costs 3 ore and 12 obsidian.""".strip().splitlines()

    blueprints = []
    for line in data[:3]:
        nums = list(map(int, re.findall(r'\d+', line)))
        bp_id = nums[0]
        ore_robot_ore = nums[1]
        clay_robot_ore = nums[2]
        obs_robot_ore = nums[3]
        obs_robot_clay = nums[4]
        geo_robot_ore = nums[5]
        geo_robot_obs = nums[6]
        blueprints.append((bp_id, ore_robot_ore, clay_robot_ore, obs_robot_ore, obs_robot_clay, geo_robot_ore, geo_robot_obs))

    def max_geodes(blueprint, time_limit):
        bp_id, ore_robot_ore, clay_robot_ore, obs_robot_ore, obs_robot_clay, geo_robot_ore, geo_robot_obs = blueprint

        max_ore_needed = max(ore_robot_ore, clay_robot_ore, obs_robot_ore, geo_robot_ore)
        max_clay_needed = obs_robot_clay
        max_obs_needed = geo_robot_obs

        best = [0]

        def dfs(time, ore_robots, clay_robots, obs_robots, geo_robots, ore, clay, obs, geodes):
            if time == 0:
                best[0] = max(best[0], geodes)
                return

            if geodes + geo_robots * time + time * (time - 1) // 2 <= best[0]:
                return

            new_ore = ore + ore_robots
            new_clay = clay + clay_robots
            new_obs = obs + obs_robots
            new_geodes = geodes + geo_robots

            can_build_geode = ore >= geo_robot_ore and obs >= geo_robot_obs
            can_build_obs = ore >= obs_robot_ore and clay >= obs_robot_clay
            can_build_clay = ore >= clay_robot_ore
            can_build_ore = ore >= ore_robot_ore

            if can_build_geode:
                dfs(time - 1, ore_robots, clay_robots, obs_robots, geo_robots + 1,
                    new_ore - geo_robot_ore, new_clay, new_obs - geo_robot_obs, new_geodes)

            if can_build_obs and obs_robots < max_obs_needed:
                dfs(time - 1, ore_robots, clay_robots, obs_robots + 1, geo_robots,
                    new_ore - obs_robot_ore, new_clay - obs_robot_clay, new_obs, new_geodes)

            if can_build_clay and clay_robots < max_clay_needed:
                dfs(time - 1, ore_robots, clay_robots + 1, obs_robots, geo_robots,
                    new_ore - clay_robot_ore, new_clay, new_obs, new_geodes)

            if can_build_ore and ore_robots < max_ore_needed:
                dfs(time - 1, ore_robots + 1, clay_robots, obs_robots, geo_robots,
                    new_ore - ore_robot_ore, new_clay, new_obs, new_geodes)

            if not (can_build_ore and can_build_clay and (can_build_obs or clay == 0) and (can_build_geode or obs == 0)):
                dfs(time - 1, ore_robots, clay_robots, obs_robots, geo_robots,
                    new_ore, new_clay, new_obs, new_geodes)

        dfs(time_limit, 1, 0, 0, 0, 0, 0, 0, 0)
        return best[0]

    result = 1
    for blueprint in blueprints:
        geodes = max_geodes(blueprint, 32)
        result *= geodes
        print(f"Blueprint {blueprint[0]}: {geodes} geodes")

    print(result)
    AOC.submit_answer(result)


if __name__ == "__main__":
    solve()
