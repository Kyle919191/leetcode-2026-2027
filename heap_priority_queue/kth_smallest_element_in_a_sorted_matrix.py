"""
LeetCode 378 - Kth Smallest Element in a Sorted Matrix

Task:
Given an `n x n` matrix where each of the rows and columns is sorted in
ascending order, return the `k`th smallest element in the matrix.

Note that it is the `k`th smallest element in sorted order, not the `k`th
distinct element.

Example 1:
Input: matrix = [[1, 5, 9], [10, 11, 13], [12, 13, 15]], k = 8
Output: 13

Example 2:
Input: matrix = [[-5]], k = 1
Output: -5
"""

import heapq

# Solution 1
# this problem is very similar to linked_list/merge k sorted linked list
# idea: we don't want to push all elements immediately because pushing and popping a large
# heap wastes time and space. we just want to push/pop some of them.

#important realization: the matrix doesn't guanratee the former elemnt is less than the later element,
#only column and row ascending. For example, 2nd row 3rd element is greater than 3rd row 1st element
def kth_smallest_sol1(matrix: list[list[int]], k: int) -> int:
    if not matrix or not matrix[0]:
        raise ValueError("matrix must be non-empty")
    if k <= 0:
        raise ValueError("k must be positive")

    n = len(matrix)
    cols = len(matrix[0])
    total = n * cols
    if k > total:
        raise ValueError("k is larger than total number of elements")

    min_heap: list[tuple[int, int, int]] = []

    # Push the first element of each row: (value, row, col).
    # why is k valid when k<n? it's because columns are sorted ascending too, so grabbing the first k
    # rows is already sufficient
    for row in range(min(n, k)):
        heapq.heappush(min_heap, (matrix[row][0], row, 0))

    # Pop k - 1 times; the top after that is the kth smallest.
    for _ in range(k - 1):
        _, row, col = heapq.heappop(min_heap)

        # Add the next element from the same row.
        if col + 1 < cols:
            heapq.heappush(min_heap, (matrix[row][col + 1], row, col + 1))
            # first each col/row initialization makes it simple: all we need is move forward
            # until no more nodes

    return heapq.heappop(min_heap)[0]
# Solution 2
def kth_smallest_sol2(matrix: list[list[int]], k: int) -> int:
    # TODO: write your second solution
    raise NotImplementedError("Implement kth_smallest_sol2")


# Solution 3 (optional)
def kth_smallest_sol3(matrix: list[list[int]], k: int) -> int:
    # TODO: write your third solution (optional)
    raise NotImplementedError("Implement kth_smallest_sol3")


# =========================================
# Simple test function (major test cases)
# =========================================
def run_basic_tests(solution_func) -> None:
    test_cases = [
        (
            [[1, 5, 9], [10, 11, 13], [12, 13, 15]],
            8,
            13,
        ),
        ([[-5]], 1, -5),
        ([[1, 2], [1, 3]], 2, 1),
        ([[1, 3, 5], [6, 7, 12], [11, 14, 14]], 6, 11),
        ([[1, 2], [3, 4]], 4, 4),
    ]

    print(f"\nTesting: {solution_func.__name__}")
    passed = 0

    for matrix, k, expected in test_cases:
        result = solution_func(matrix, k)
        if result == expected:
            passed += 1
            print(f"PASS | matrix={matrix}, k={k} -> {result}")
        else:
            print(
                f"FAIL | matrix={matrix}, k={k} -> got {result}, "
                f"expected {expected}"
            )

    print(f"Passed {passed}/{len(test_cases)} test cases.")


if __name__ == "__main__":
    run_basic_tests(kth_smallest_sol1)
    # run_basic_tests(kth_smallest_sol2)
    # run_basic_tests(kth_smallest_sol3)


# =========================
# Notes (write here later)
# =========================
# - Key insight:
# - Use min-heap as a k-way merge frontier over sorted rows.
# - Time complexity notes: O(k log n), where n is matrix dimension.
# - Space complexity notes: O(min(n, k)) for heap size.
# - Common mistakes:
# - Follow-up ideas:
