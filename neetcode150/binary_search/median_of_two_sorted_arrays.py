"""
LeetCode 4 - Median of Two Sorted Arrays
"""


def find_median_sorted_arrays_sol1(nums1: list[int], nums2: list[int]) -> float:
    A = nums1
    B = nums2

    if len(nums1) > len(nums2):
        A, B = B, A
    
    total = len(nums1)+len(nums2)
    half = total // 2 # floor divison, meaning left half has equal or less elements than right half

    left = 0
    right = len(A) # use the shorter array, more convenient
    # len(A) instead of len(A)-1 because it's the number of elements A contributes to the left side not index

    while left <= right:
        i = (left + right) // 2 # use mid, guess that middle of the shorter array is the best split.
        # i is how much A should contribute to left, j is how much B should contribute to left
        j = half - i

        Aleft = A[i - 1] if i > 0 else float("-inf") # patch the four numbers adjacent to the splits, because we'll do comparsions later
        # in the case when Aleft has no elements(i says contribute 0), we can still put -inf
        Aright = A[i] if i < len(A) else float("inf")
        Bleft = B[j - 1] if j > 0 else float("-inf")
        Bright = B[j] if j < len(B) else float("inf")

        # TODO-TALK: Correct partition means left max <= right min on both sides.
        if Aleft<=Bright and Bleft<=Aright: # check for correct split: Aleft<Aright is assumed
            if total % 2: # if total length of A+B is odd, pick middle number. else, average the middle, which
                # should be the largest one of the left and smallest one of the rgight
                return min(Aright, Bright) # median on right because we did half = total // 2
            else:
                return (max(Aleft, Bleft)+min(Aright, Bright)) / 2
        elif Aleft>Bright: # we consumed too much left for A, shrink that left side of A to make A LHS smaller and A RHS bigger
            right = i - 1 
        else:
            left = i + 1 # mke A LHS bigger, RHS smaller





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
    run_basic_tests(find_median_sorted_arrays_sol1)
    # run_basic_tests(find_median_sorted_arrays_sol2)
    # run_basic_tests(find_median_sorted_arrays_sol3)

