"""
Two Sum Target - Return All Unique Value Pairs

Related:
- Very close to LeetCode LCCI 16.24 - Pairs With Sum.
- Not the same as LeetCode 1 / 167 (those return one pair or indices).

Task:
Given an integer array `nums` and an integer `target`, return all unique pairs
`[a, b]` such that `a + b == target`.

Rules:
- Return element values, not indices.
- Do not include duplicate pairs.
- [a, b] and [b, a] are considered the same pair.

Example:
Input: nums = [1, 3, 1, 2, 2, 3], target = 4
Output: [[1, 3], [2, 2]]
"""


# Solution 1
def two_sum_target_sol1(nums: list[int], target: int) -> list[list[int]]:
    # the nums array must be sorted
    nums.sort()
    lo, hi = 0, len(nums) - 1
    res = []
    while lo < hi:
        sum = nums[lo] + nums[hi]
        left, right = nums[lo], nums[hi]
        if sum < target:
            while lo < hi and nums[lo] == left: # if a pair don't work, we skip all copies of the value we're trying to move away from
                lo += 1 # keep incrementing until it's no longer valued left
        elif sum > target:
            while lo < hi and nums[hi] == right: 
                hi -= 1
        else:
            res.append([left, right]) # in case of match, do this increment on both left and right
            # you want to move both toward the middle because that's the way to possibly find more pairss
            while lo < hi and nums[lo] == left: 
                lo += 1
            while lo < hi and nums[hi] == right: 
                hi -= 1
    return res


# Solution 2
def two_sum_target_sol2(nums: list[int], target: int) -> list[list[int]]:
    # TODO: write your second solution
    raise NotImplementedError("Implement two_sum_target_sol2")


# Solution 3 (optional)
def two_sum_target_sol3(nums: list[int], target: int) -> list[list[int]]:
    # TODO: write your third solution (optional)
    raise NotImplementedError("Implement two_sum_target_sol3")


# Optional alias matching requested signature style.
def twoSumTarget(nums: list[int], target: int) -> list[list[int]]:
    return two_sum_target_sol1(nums, target)


def normalize_pairs(pairs: list[list[int]]) -> list[list[int]]:
    # Normalize for test comparison:
    # 1) each pair sorted
    # 2) overall list sorted
    # 3) duplicates removed
    normalized = [sorted(pair) for pair in pairs]
    normalized = sorted({(a, b) for a, b in normalized})
    return [[a, b] for a, b in normalized]


# =========================================
# Simple test function (major test cases)
# =========================================
def run_basic_tests(solution_func) -> None:
    test_cases = [
        ([1, 3, 1, 2, 2, 3], 4, [[1, 3], [2, 2]]),
        ([1, 1, 1, 1], 2, [[1, 1]]),
        ([0, 0, 0], 0, [[0, 0]]),
        ([-1, 5, 3, 1, 2, 4, -1], 4, [[-1, 5], [1, 3]]),
        ([1, 2, 3], 100, []),
        ([], 5, []),
    ]

    print(f"\nTesting: {solution_func.__name__}")
    passed = 0

    for nums, target, expected in test_cases:
        result = solution_func(nums[:], target)
        got_norm = normalize_pairs(result)
        exp_norm = normalize_pairs(expected)
        if got_norm == exp_norm:
            passed += 1
            print(f"PASS | nums={nums}, target={target} -> {got_norm}")
        else:
            print(
                f"FAIL | nums={nums}, target={target} -> got {got_norm}, "
                f"expected {exp_norm}"
            )

    print(f"Passed {passed}/{len(test_cases)} test cases.")


if __name__ == "__main__":
    # run_basic_tests(two_sum_target_sol1)
    # run_basic_tests(two_sum_target_sol2)
    # run_basic_tests(two_sum_target_sol3)
    pass


# =========================
# Notes (write here later)
# =========================
# - Key insight:
# - Time complexity notes:
# - Space complexity notes:
# - Common mistakes:
# - Follow-up ideas:
