"""
LeetCode 42 - Trapping Rain Water
"""

# formula: water_at_i = min(max_left, max_right) - height[i]
# where max_left[i] = max(height[0:i+1]), max_right[i] = max(height[i:])
def trap_sol1(height: list[int]) -> int:
    left = 0
    right = len(height) - 1
    max_left = max_right = 0
    water = 0
    while left < right:
        if height[left] <= height[right]:
            # TODO-TALK: Left side is limiting now, so left position is decidable.
            max_left = max(max_left, height[left])
            # since left height is smaller, we "process" left height by the formula
            water += max_left - height[left]
            left += 1
        else:
            # TODO-TALK: Right side is limiting now, so left position is decidable.
            max_right = max(max_right, height[right])
            water += max_right - height[right]
            right -= 1
    return water



def trap_sol2(height: list[int]) -> int:
    raise NotImplementedError("Implement trap_sol2")


def trap_sol3(height: list[int]) -> int:
    raise NotImplementedError("Implement trap_sol3")


def run_basic_tests(solution_func) -> None:
    test_cases = [
        ([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1], 6),
        ([4, 2, 0, 3, 2, 5], 9),
        ([], 0),
        ([1, 2, 3], 0),
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
    run_basic_tests(trap_sol1)
    # run_basic_tests(trap_sol2)
    # run_basic_tests(trap_sol3)
    pass
