"""
LeetCode 54 - Spiral Matrix

Task:
Given an `m x n` matrix, return all elements of the matrix in spiral order.

Example 1:
Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,3,6,9,8,7,4,5]

Example 2:
Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]
"""


# Solution 1
def spiral_order_sol1(matrix: list[list[int]]) -> list[int]:
    # the spiral idea: first go right, then down, then left, then up, which results in a smaller spiral
    row = len(matrix)
    column = len(matrix[0])
    up, down = 0, row - 1
    left, right = 0, column - 1
    result = []

    # if equal, the entire matrix is traversed
    while len(result) < row * column:
        if up <= down: #<= because when they're equal that means there's still a row to travers
            for i in range(left, right+1): # +1 because range is exclusive and we did right=column -1
                result.append(matrix[up][i]) # traverse the top row
            up += 1 # move up to a lower row 
        
        if left <= right:
            for i in range(up, down+1):
                result.append(matrix[i][right]) #traverse right most column
            right -= 1
        
        if up <= down: # that means we can still traverse row, but this one right to left
            for i in range(right, left-1, -1): #left -1 because range exclusive
                result.append(matrix[down][i]) 
            down -= 1 # move down up a row
        
        if left <= right:
            for i in range(down, up-1, -1):
                result.append(matrix[i][left]) #traverse left most column bottom up
            left += 1
    return result



# Solution 2
def spiral_order_sol2(matrix: list[list[int]]) -> list[int]:
    # TODO: write your second solution
    raise NotImplementedError("Implement spiral_order_sol2")


# Solution 3 (optional)
def spiral_order_sol3(matrix: list[list[int]]) -> list[int]:
    # TODO: write your third solution (optional)
    raise NotImplementedError("Implement spiral_order_sol3")


# =========================================
# Simple test function (major test cases)
# =========================================
def run_basic_tests(solution_func) -> None:
    test_cases = [
        ([[1, 2, 3], [4, 5, 6], [7, 8, 9]], [1, 2, 3, 6, 9, 8, 7, 4, 5]),
        (
            [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]],
            [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7],
        ),
        ([[1]], [1]),
        ([[1, 2, 3, 4]], [1, 2, 3, 4]),
        ([[1], [2], [3]], [1, 2, 3]),
    ]

    print(f"\nTesting: {solution_func.__name__}")
    passed = 0

    for matrix, expected in test_cases:
        result = solution_func([row[:] for row in matrix])
        if result == expected:
            passed += 1
            print(f"PASS | matrix={matrix} -> {result}")
        else:
            print(f"FAIL | matrix={matrix} -> got {result}, expected {expected}")

    print(f"Passed {passed}/{len(test_cases)} test cases.")


if __name__ == "__main__":
    run_basic_tests(spiral_order_sol1)
    # run_basic_tests(spiral_order_sol2)
    # run_basic_tests(spiral_order_sol3)


# =========================
# Notes (write here later)
# =========================
# - Key insight:
# - Time complexity notes:
# - Space complexity notes:
# - Common mistakes:
# - Follow-up ideas:
