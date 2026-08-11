"""
LeetCode 48 - Rotate Image

Task:
You are given an n x n 2D matrix representing an image. Rotate the image by 90
degrees (clockwise).

You have to rotate the image in-place, which means you have to modify the input
2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.

Example 1:
Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [[7,4,1],[8,5,2],[9,6,3]]

Example 2:
Input: matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
Output: [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]
"""

# general reverse list function, same idea as reverse_words in a string
def reverse(arr):
    left, right = 0, len(arr) -1
    while left < right: # if left=right, the swap is meaningless
        temp = arr[left]
        arr[left] = arr[right]
        arr[right] = temp
        left += 1
        right -= 1
        # helper, no need to return


# Solution 1
def rotate_image_sol1(matrix: list[list[int]]) -> None:
    # glancing at the problem, the solution is simple: first row should be come third column(or last column), etc
    # but how we actually do it efficiently? 
    # here's the trick: first turn row1 to column1: simple
    # then reverse each row, effectively bring column1 to column3
    
    # to turn row1 into col1, we swap along the y=x line:
    n = len(matrix)
    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    
    # next, call reverse
    for row in matrix:
        reverse(row)
    


# Solution 2
def rotate_image_sol2(matrix: list[list[int]]) -> None:
    # TODO: write your second solution
    raise NotImplementedError("Implement rotate_image_sol2")


# Solution 3 (optional)
def rotate_image_sol3(matrix: list[list[int]]) -> None:
    # TODO: write your third solution (optional)
    raise NotImplementedError("Implement rotate_image_sol3")


# =========================================
# Simple test function (major test cases)
# =========================================
def run_basic_tests(solution_func) -> None:
    test_cases = [
        (
            [[1, 2, 3], [4, 5, 6], [7, 8, 9]],
            [[7, 4, 1], [8, 5, 2], [9, 6, 3]],
        ),
        (
            [[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]],
            [[15, 13, 2, 5], [14, 3, 4, 1], [12, 6, 8, 9], [16, 7, 10, 11]],
        ),
        ([[1]], [[1]]),
        ([[1, 2], [3, 4]], [[3, 1], [4, 2]]),
    ]

    print(f"\nTesting: {solution_func.__name__}")
    passed = 0

    for matrix, expected in test_cases:
        arr = [row[:] for row in matrix]
        solution_func(arr)
        if arr == expected:
            passed += 1
            print(f"PASS | matrix={matrix} -> {arr}")
        else:
            print(f"FAIL | matrix={matrix} -> got {arr}, expected {expected}")

    print(f"Passed {passed}/{len(test_cases)} test cases.")


if __name__ == "__main__":
    run_basic_tests(rotate_image_sol1)
    # run_basic_tests(rotate_image_sol2)
    # run_basic_tests(rotate_image_sol3)



# =========================
# Notes (write here later)
# =========================
# - Key insight:
# - Time complexity notes:
# - Space complexity notes:
# - Common mistakes:
# - Follow-up ideas:
