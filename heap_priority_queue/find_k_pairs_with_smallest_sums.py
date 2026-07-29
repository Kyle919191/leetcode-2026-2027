"""
LeetCode 373 - Find K Pairs with Smallest Sums

Task:
You are given two integer arrays `nums1` and `nums2` sorted in non-decreasing
order and an integer `k`.

Define a pair `(u, v)` where one element comes from `nums1` and one comes from
`nums2`.

Return the `k` pairs with the smallest sums.

Example 1:
Input: nums1 = [1, 7, 11], nums2 = [2, 4, 6], k = 3
Output: [[1, 2], [1, 4], [1, 6]]

Example 2:
Input: nums1 = [1, 1, 2], nums2 = [1, 2, 3], k = 2
Output: [[1, 1], [1, 1]]
"""
import heapq

# Visualization as merge k sorted linked lists:
# nums1 = [1, 7, 11], nums2 = [2, 4, 6]
# All pairs formed can be abstracted into three sorted linked lists:
# [1, 2] -> [1, 4] -> [1, 6]
# [7, 2] -> [7, 4] -> [7, 6]
# [11, 2] -> [11, 4] -> [11, 6]
# wth this, we can transform two lists into a matrix of nums1 rows and nums2 columns

# Solution 1
# again, also variant of linked list/ merge k sorted list
def k_smallest_pairs_sol1(
    nums1: list[int],
    nums2: list[int],
    k: int,
) -> list[list[int]]:
    
    if not nums1 or not nums2 or k<=0:
        return []
    
    rows = len(nums1)
    columns = len(nums2)

    result: list[list[int]] = []
    # (pair_sum, i, j) where pair is (nums1[i], nums2[j])
    min_heap: list[tuple[int, int, int]] = []

    for i in range (min(rows, k)):
        heapq.heappush(min_heap, (nums1[i]+nums2[0], i, 0))
    
    while min_heap and len(result)<k: #len(result)<k: haven't gotten k solutions
        sum, i, j = heapq.heappop(min_heap)
        result.append([nums1[i], nums2[j]])

        if j+1 < columns:
            heapq.heappush(min_heap, (nums1[i]+nums2[j+1], i, j+1))
    return result



# Solution 2
def k_smallest_pairs_sol2(
    nums1: list[int],
    nums2: list[int],
    k: int,
) -> list[list[int]]:
    # TODO: write your second solution
    raise NotImplementedError("Implement k_smallest_pairs_sol2")


# Solution 3 (optional)
def k_smallest_pairs_sol3(
    nums1: list[int],
    nums2: list[int],
    k: int,
) -> list[list[int]]:
    # TODO: write your third solution (optional)
    raise NotImplementedError("Implement k_smallest_pairs_sol3")


def _normalize_pairs(pairs: list[list[int]]) -> list[tuple[int, int]]:
    # Compare results regardless of tie-order in valid outputs.
    return sorted((a, b) for a, b in pairs)


# =========================================
# Simple test function (major test cases)
# =========================================
def run_basic_tests(solution_func) -> None:
    test_cases = [
        ([1, 7, 11], [2, 4, 6], 3, [[1, 2], [1, 4], [1, 6]]),
        ([1, 1, 2], [1, 2, 3], 2, [[1, 1], [1, 1]]),
        ([1, 2], [3], 3, [[1, 3], [2, 3]]),
        ([], [1, 2], 3, []),
        ([1, 2], [], 3, []),
    ]

    print(f"\nTesting: {solution_func.__name__}")
    passed = 0

    for nums1, nums2, k, expected in test_cases:
        result = solution_func(nums1, nums2, k)
        ok = _normalize_pairs(result) == _normalize_pairs(expected)
        if ok:
            passed += 1
            print(f"PASS | nums1={nums1}, nums2={nums2}, k={k} -> {result}")
        else:
            print(
                f"FAIL | nums1={nums1}, nums2={nums2}, k={k} -> "
                f"got {result}, expected {expected}"
            )

    print(f"Passed {passed}/{len(test_cases)} test cases.")


if __name__ == "__main__":
    run_basic_tests(k_smallest_pairs_sol1)
    # run_basic_tests(k_smallest_pairs_sol2)
    # run_basic_tests(k_smallest_pairs_sol3)


# =========================
# Notes (write here later)
# =========================
# - Key insight:
# - Time complexity notes:
# - Space complexity notes:
# - Common mistakes:
# - Follow-up ideas:
