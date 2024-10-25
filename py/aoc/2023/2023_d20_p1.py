from aoc.helper import download_input, submit_answer
from aoc.util import benchmark


@benchmark
def run():
    download_input(2023, 20)

    module_conf_spec = """
broadcaster -> a, b, c
%a -> b
%b -> c
%c -> inv
&inv -> a
    """.strip().splitlines()

    module_conf = build_module_configuration(module_conf_spec)
    print(module_conf)
    C = press_button(module_conf, 1000)
    print(C)


def press_button(module_configuration, n):
    high_count = 0
    low_count = 0

    next_high = []
    next_low = module_configuration["broadcaster"][2]
    low_count += 1

    for i, _ in enumerate(range(n), start=1):
        print(f"====Iteration {i}======")

        nh = []
        nl = []

        for nxt in next_low:
            low_count += 1
            mt, s, d = module_configuration[nxt]
            if mt == "flipflop":
                nh.extend(d)
                module_configuration[nxt][1] = "on" if s == "off" else "on"
            elif mt == "conjunction":
                module_configuration[nxt][1] = "low"
                if s == "low":
                    nh.extend(d)
                else:
                    nl.extend(d)
            else:
                raise RuntimeError("Unknown module type")

        for nxt in nh:
            high_count += 1
            mt, s, d = module_configuration[nxt]
            if mt == "conjunction":
                module_configuration[nxt][1] = "high"
                if s == "low":
                    nh.extend(d)
                else:
                    nl.extend(d)

        next_high = nh
        next_low = nl

        print(f"====Iteration Complete======")

    print(low_count, high_count)
    return high_count * low_count


def build_module_configuration(module_conf_spec):
    module_configuration = {}
    for line in module_conf_spec:
        name, destinations = line.split(" -> ")
        destinations = [d.strip() for d in destinations.split(",")]
        if "%" in name:
            name = name[1:]
            module_type = "flipflop"
            initial_state = "off"
        elif "&" in name:
            name = name[1:]
            module_type = "conjunction"
            initial_state = "low"
        elif "broadcaster" in name:
            module_type = "broadcaster"
            initial_state = "n/a"
        else:
            raise RuntimeError("Unknown module")
        module_configuration[name] = [module_type, initial_state, destinations]
    return module_configuration


if __name__ == "__main__":
    run()
