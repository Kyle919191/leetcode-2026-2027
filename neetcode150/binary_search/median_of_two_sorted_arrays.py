"""
LeetCode 4 - Median of Two Sorted Arrays
"""


def find_median_sorted_arrays_sol1(nums1: list[int], nums2: list[int]) -> float:
    raise NotImplementedError("Implement find_median_sorted_arrays_sol1")


def find_median_sorted_arrays_sol2(nums1: list[int], nums2: list[int]) -> float:
    raise NotImplementedError("Implement find_median_sorted_arrays_sol2")


def find_median_sorted_arrays_sol3(nums1: list[int], nums2: list[int]) -> float:
    raise NotImplementedError("Implement find_median_sorted_arrays_sol3")


def run_basic_tests(solution_func) -> None:
    test_cases = [
        ([1, 3], [2], 2.0),
        ([1, 2], [3, 4], 2.5),
        ([0, 0], [0, 0], 0.0),
    ]
    print(f"\nTesting: {solution_func.__name__}")
    passed = 0
    for nums1, nums2, expected in test_cases:
        got = solution_func(nums1[:], nums2[:])
        if abs(got - expected) < 1e-9:
            passed += 1
            print(f"PASS | nums1={nums1}, nums2={nums2} -> {got}")
        else:
            print(f"FAIL | nums1={nums1}, nums2={nums2} -> got {got}, expected {expected}")
    print(f"Passed {passed}/{len(test_cases)} test cases.")


if __name__ == "__main__":
    # run_basic_tests(find_median_sorted_arrays_sol1)
    # run_basic_tests(find_median_sorted_arrays_sol2)
    # run_basic_tests(find_median_sorted_arrays_sol3)
    pass
