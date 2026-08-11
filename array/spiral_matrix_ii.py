"""
LeetCode 59 - Spiral Matrix II

Task:
Given a positive integer `n`, generate an `n x n` matrix filled with elements
from 1 to `n^2` in spiral order.

Example 1:
Input: n = 3
Output: [[1,2,3],[8,9,4],[7,6,5]]

Example 2:
Input: n = 1
Output: [[1]]
"""


# Solution 1
def generate_matrix_sol1(n: int) -> list[list[int]]:
    # very similar to spiral matrix 
    matrix = [[0]*n for _ in range(n)]
    upper_bound = 0
    lower_bound = n - 1
    left_bound = 0
    right_bound = n - 1
    # the number to be filled in the matrix
    num = 1

    while num <= n * n:
        if upper_bound <= lower_bound:
            # traverse from left to right at the top
            for j in range(left_bound, right_bound + 1):
                matrix[upper_bound][j] = num
                num += 1
            # move the upper bound down
            upper_bound += 1

        if left_bound <= right_bound:
            # traverse from top to bottom on the right
            for i in range(upper_bound, lower_bound + 1):
                matrix[i][right_bound] = num
                num += 1
            # move the right bound left
            right_bound -= 1

        if upper_bound <= lower_bound:
            # traverse from right to left at the bottom
            for j in range(right_bound, left_bound - 1, -1):
                matrix[lower_bound][j] = num
                num += 1
            # move the lower bound up
            lower_bound -= 1

        if left_bound <= right_bound:
            # traverse from bottom to top on the left
            for i in range(lower_bound, upper_bound - 1, -1):
                matrix[i][left_bound] = num
                num += 1
            # move the left bound right
            left_bound += 1

    return matrix


# Solution 2
def generate_matrix_sol2(n: int) -> list[list[int]]:
    # TODO: write your second solution
    raise NotImplementedError("Implement generate_matrix_sol2")


# Solution 3 (optional)
def generate_matrix_sol3(n: int) -> list[list[int]]:
    # TODO: write your third solution (optional)
    raise NotImplementedError("Implement generate_matrix_sol3")


# =========================================
# Simple test function (major test cases)
# =========================================
def run_basic_tests(solution_func) -> None:
    test_cases = [
        (1, [[1]]),
        (2, [[1, 2], [4, 3]]),
        (3, [[1, 2, 3], [8, 9, 4], [7, 6, 5]]),
        (4, [[1, 2, 3, 4], [12, 13, 14, 5], [11, 16, 15, 6], [10, 9, 8, 7]]),
    ]

    print(f"\nTesting: {solution_func.__name__}")
    passed = 0

    for n, expected in test_cases:
        result = solution_func(n)
        if result == expected:
            passed += 1
            print(f"PASS | n={n} -> {result}")
        else:
            print(f"FAIL | n={n} -> got {result}, expected {expected}")

    print(f"Passed {passed}/{len(test_cases)} test cases.")


if __name__ == "__main__":
    run_basic_tests(generate_matrix_sol1)
    # run_basic_tests(generate_matrix_sol2)
    # run_basic_tests(generate_matrix_sol3)


# =========================
# Notes (write here later)
# =========================
# - Key insight:
# - Time complexity notes:
# - Space complexity notes:
# - Common mistakes:
# - Follow-up ideas:
