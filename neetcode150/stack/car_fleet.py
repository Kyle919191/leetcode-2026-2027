"""
LeetCode 853 - Car Fleet
"""


def car_fleet_sol1(target: int, position: list[int], speed: list[int]) -> int:
    # sort by greatest distance(closest to target)
    # [(10, 2), (8, 4), (5, 1), (3, 3), (0, 1)]
    pairs = sorted(zip(position, speed), reverse=True)
    latest_time = 0.0
    fleet_num = 0
    for p, s in pairs:
        current_time = (target-p) / s
        # the caveat is that a car can only become a fleet with the car directly in front of it, hence stack idea
        # for example, say in fleet 1 we have two cars, each with hour 1, 1; second fleet 1 car, hour 4. now say a 
        # fourth car comes in with speed 1. it will be a part of second fleet, not first fleet.
        # TODO-TALK: A larger time behind means it cannot catch up, so new fleet.
        if current_time > latest_time:
            fleet_num += 1
            latest_time = current_time
    return fleet_num




def car_fleet_sol2(target: int, position: list[int], speed: list[int]) -> int:
    raise NotImplementedError("Implement car_fleet_sol2")


def car_fleet_sol3(target: int, position: list[int], speed: list[int]) -> int:
    raise NotImplementedError("Implement car_fleet_sol3")


def run_basic_tests(solution_func) -> None:
    test_cases = [
        (12, [10, 8, 0, 5, 3], [2, 4, 1, 1, 3], 3),
        (10, [3], [3], 1),
        (100, [0, 2, 4], [4, 2, 1], 1),
    ]
    print(f"\nTesting: {solution_func.__name__}")
    passed = 0
    for target, position, speed, expected in test_cases:
        got = solution_func(target, position[:], speed[:])
        if got == expected:
            passed += 1
            print(f"PASS | target={target}, position={position}, speed={speed} -> {got}")
        else:
            print(f"FAIL | target={target}, position={position}, speed={speed} -> got {got}, expected {expected}")
    print(f"Passed {passed}/{len(test_cases)} test cases.")


if __name__ == "__main__":
    run_basic_tests(car_fleet_sol1)
    # run_basic_tests(car_fleet_sol2)
    # run_basic_tests(car_fleet_sol3)

