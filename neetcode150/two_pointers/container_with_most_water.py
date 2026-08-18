"""
LeetCode 11 - Container With Most Water
"""


def max_area_sol1(height: list[int]) -> int:
    left = 0
    right = len(height) - 1
    max_area = 0

    while left < right: # when left=right, width is essentially 0
        w = right - left
        h = min(height[left], height[right])
        max_area = max(max_area, w*h)

        if height[left] <= height[right]:
            # TODO-TALK: Move shorter side hoping to find a taller boundary.
            # since height is constrained by the shorter bar and we start with the greatest width,
            # the only way we can possibly increase area is to move the shorter bar, hoping to 
            # find the taller bar at the expense of reduced width. 
            # this is classic two pointer like two_sum_sorted
            left += 1
        else:
            right -= 1
    return max_area




def max_area_sol2(height: list[int]) -> int:
    raise NotImplementedError("Implement max_area_sol2")


def max_area_sol3(height: list[int]) -> int:
    raise NotImplementedError("Implement max_area_sol3")


def run_basic_tests(solution_func) -> None:
    test_cases = [
        ([1, 8, 6, 2, 5, 4, 8, 3, 7], 49),
        ([1, 1], 1),
        ([4, 3, 2, 1, 4], 16),
    ]
    print(f"\nTesting: {solution_func.__name__}")
    passed = 0
    for height, expected in test_cases:
        got = solution_func(height[:])
        if got == expected:
            passed += 1
            print(f"PASS | height={height} -> {got}")
        else:
            print(f"FAIL | height={height} -> got {got}, expected {expected}")
    print(f"Passed {passed}/{len(test_cases)} test cases.")


if __name__ == "__main__":
    run_basic_tests(max_area_sol1)
    # run_basic_tests(max_area_sol2)
    # run_basic_tests(max_area_sol3)

