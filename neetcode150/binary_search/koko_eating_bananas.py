"""
LeetCode 875 - Koko Eating Bananas
"""


def min_eating_speed_sol1(piles: list[int], h: int) -> int:
    def can_finish(speed: int) -> bool:
        hours = 0
        for pile in piles:
            hours += (pile + speed - 1) // speed # equivalent to math.ceil(pile / speed)
        return hours <= h
    
    left = 1 # min speed should be 1
    right = max(piles) # if our speed is the max pile, it will guanrantee to succeed within len(piles) hours

    while left <= right:
        mid = left + (right - left) // 2

        # TODO-TALK: If mid speed works, try smaller; otherwise speed up.
        if can_finish(mid):
            answer = mid # early track, in case next iteration breaks the while loop
            # there's also the pattern for left < right case: right=mid, left=mid+1, return left
            right = mid - 1
        else:
            left = mid + 1
    return answer # in this case, the question will always be found at left == right because we're trying to converge to one number
    # instead of just looking for a target


def min_eating_speed_sol2(piles: list[int], h: int) -> int:
    raise NotImplementedError("Implement min_eating_speed_sol2")


def min_eating_speed_sol3(piles: list[int], h: int) -> int:
    raise NotImplementedError("Implement min_eating_speed_sol3")


def run_basic_tests(solution_func) -> None:
    test_cases = [
        ([3, 6, 7, 11], 8, 4),
        ([30, 11, 23, 4, 20], 5, 30),
        ([30, 11, 23, 4, 20], 6, 23),
    ]
    print(f"\nTesting: {solution_func.__name__}")
    passed = 0
    for piles, h, expected in test_cases:
        got = solution_func(piles[:], h)
        if got == expected:
            passed += 1
            print(f"PASS | piles={piles}, h={h} -> {got}")
        else:
            print(f"FAIL | piles={piles}, h={h} -> got {got}, expected {expected}")
    print(f"Passed {passed}/{len(test_cases)} test cases.")


if __name__ == "__main__":
    run_basic_tests(min_eating_speed_sol1)
    # run_basic_tests(min_eating_speed_sol2)
    # run_basic_tests(min_eating_speed_sol3)

