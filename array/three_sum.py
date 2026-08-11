"""
3Sum Target (Generalized)

Task:
Given an integer array `nums`, return all the triplets `[nums[i], nums[j], nums[k]]`
such that `i != j`, `i != k`, and `j != k`, and
`nums[i] + nums[j] + nums[k] == target`.

The solution set must not contain duplicate triplets.

Example 1:
Input: nums = [-1,0,1,2,-1,-4], target = 0
Output: [[-1,-1,2],[-1,0,1]]

Example 2:
Input: nums = [1,2,3,4,5], target = 9
Output: [[1,3,5],[2,3,4]]

Example 3:
Input: nums = [0,0,0], target = 0
Output: [[0,0,0]]
"""

# similar as two_sum_target_all_pairs
def two_sum_deduplicate_helper(nums, start, target):
    # nums already sorted from three_sum
    result = []
    low, high = start, len(nums) - 1
    
    while low < high:
        left_num = nums[low]
        right_num = nums[high]
        sum = left_num+right_num

        if sum < target:
            while low<high and nums[low] == left_num:
                low += 1
        elif sum > target:
            while low<high and nums[high] == right_num:
                high -= 1
        else:
            result.append([left_num, right_num]) 
            while low<high and nums[low] == left_num:
                low += 1
            while low<high and nums[high] == right_num:
                high -= 1
    return result

# Solution 1
def three_sum_target_sol1(nums: list[int], target: int) -> list[list[int]]:
    # - Sort nums first.
    # - Fix nums[i] as the first number.
    # - Then run a Two Sum "all unique value pairs" search on the suffix
    #   [i+1 ... end] for target = target - nums[i].

    nums.sort()
    result = []

    i=0
    n=len(nums)
    while i < n:
        current = nums[i]
        pairs = two_sum_deduplicate_helper(nums, i+1, target-current)
        if not pairs: 
            i+=1
            continue
        for pair in pairs:
            pair.append(current)
            result.append(pair)
        
        # duplicates of other two numbers are handled in two sum helper
        # but we still need to handle the duplicate case where i+1 value is same as i value
        # "The key to avoid duplicates is to make sure the first number is not repeated. For the other two numbers, our reused twoSumTarget function already handles duplicates"
        while i < n - 1 and current == nums[i + 1]: # <n+1 to prevent out of bounds when we do nums[i+1]
            i += 1
        i += 1
    return result





# Solution 2
def three_sum_target_sol2(nums: list[int], target: int) -> list[list[int]]:
    # TODO: write your second solution
    raise NotImplementedError("Implement three_sum_target_sol2")


# Solution 3 (optional)
def three_sum_target_sol3(nums: list[int], target: int) -> list[list[int]]:
    # TODO: write your third solution (optional)
    raise NotImplementedError("Implement three_sum_target_sol3")


def threeSum(nums: list[int]) -> list[list[int]]:
    # Optional compatibility alias for classic LeetCode 15 behavior.
    return three_sum_target_sol1(nums, 0)


def normalize_triplets(triplets: list[list[int]]) -> list[list[int]]:
    normalized = [sorted(t) for t in triplets]
    normalized = sorted({(a, b, c) for a, b, c in normalized})
    return [[a, b, c] for a, b, c in normalized]


# =========================================
# Simple test function (major test cases)
# =========================================
def run_basic_tests(solution_func) -> None:
    test_cases = [
        ([-1, 0, 1, 2, -1, -4], 0, [[-1, -1, 2], [-1, 0, 1]]),
        ([1, 2, 3, 4, 5], 9, [[1, 3, 5], [2, 3, 4]]),
        ([0, 0, 0], 0, [[0, 0, 0]]),
        ([0, 0, 0, 0], 1, []),
        ([-2, 0, 1, 1, 2], 0, [[-2, 0, 2], [-2, 1, 1]]),
        ([3, -2, 1, 0], 2, [[-2, 1, 3]]),
    ]

    print(f"\nTesting: {solution_func.__name__}")
    passed = 0

    for nums, target, expected in test_cases:
        result = solution_func(nums[:], target)
        got_norm = normalize_triplets(result)
        exp_norm = normalize_triplets(expected)
        if got_norm == exp_norm:
            passed += 1
            print(f"PASS | nums={nums}, target={target} -> {got_norm}")
        else:
            print(
                f"FAIL | nums={nums}, target={target} -> "
                f"got {got_norm}, expected {exp_norm}"
            )

    print(f"Passed {passed}/{len(test_cases)} test cases.")


if __name__ == "__main__":
    run_basic_tests(three_sum_target_sol1)
    # run_basic_tests(three_sum_target_sol2)
    # run_basic_tests(three_sum_target_sol3)



# =========================
# Notes (write here later)
# =========================
# - Key insight:
# - Time complexity notes:
# - Space complexity notes:
# - Common mistakes:
# - Follow-up ideas:
