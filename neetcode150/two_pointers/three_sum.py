"""
LeetCode 15 - 3Sum
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


def three_sum_sol1(nums: list[int]) -> list[list[int]]:
    # TODO-TALK: I will sort first so duplicate handling and two-pointer search become easy.
    # TODO-TALK: Then I fix one value and solve two-sum on the suffix for target minus that value.
    # TODO-TALK: I skip duplicates for the fixed value and also inside two-sum helper.
    target = 0
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


def three_sum_sol2(nums: list[int]) -> list[list[int]]:
    raise NotImplementedError("Implement three_sum_sol2")


def three_sum_sol3(nums: list[int]) -> list[list[int]]:
    raise NotImplementedError("Implement three_sum_sol3")


def normalize(triplets: list[list[int]]) -> list[list[int]]:
    return sorted({tuple(sorted(t)) for t in triplets})


def run_basic_tests(solution_func) -> None:
    test_cases = [
        ([-1, 0, 1, 2, -1, -4], [[-1, -1, 2], [-1, 0, 1]]),
        ([0, 1, 1], []),
        ([0, 0, 0], [[0, 0, 0]]),
    ]
    print(f"\nTesting: {solution_func.__name__}")
    passed = 0
    for nums, expected in test_cases:
        got = solution_func(nums[:])
        if normalize(got) == normalize(expected):
            passed += 1
            print(f"PASS | nums={nums} -> {got}")
        else:
            print(f"FAIL | nums={nums} -> got {got}, expected {expected}")
    print(f"Passed {passed}/{len(test_cases)} test cases.")


if __name__ == "__main__":
    # run_basic_tests(three_sum_sol1)
    # run_basic_tests(three_sum_sol2)
    # run_basic_tests(three_sum_sol3)
    pass
