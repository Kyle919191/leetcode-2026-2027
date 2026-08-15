"""
LeetCode 304 - Range Sum Query 2D - Immutable

Task:
Given a 2D matrix `matrix`, handle multiple queries of the following type:

- Calculate the sum of the elements of matrix inside the rectangle defined by
  its upper-left corner `(row1, col1)` and lower-right corner `(row2, col2)`.

Implement the `NumMatrix` class:
- `NumMatrix(matrix)` initializes the object with the integer matrix `matrix`.
- `sumRegion(row1, col1, row2, col2)` returns the sum of the elements of
  `matrix` inside the rectangle.

Example:
Input:
["NumMatrix","sumRegion","sumRegion","sumRegion"]
[[[[3,0,1,4,2],[5,6,3,2,1],[1,2,0,1,5],[4,1,0,1,7],[1,0,3,0,5]]],
 [2,1,4,3], [1,1,2,2], [1,2,2,4]]
Output:
[null, 8, 11, 12]
"""


# Solution 1
class NumMatrixSol1:
    def __init__(self, matrix: list[list[int]]):
        row = len(matrix)
        col = len(matrix[0])
        if row == 0 or col == 0:
            return
        self.prefix_sum = [[0] * (col+1) for _ in range(row+1)] # row is outer loop. +1 because prefix sum has extra length

        for i in range(1, row+1):
            for j in range(1, col+1):
                # prefix_sum[i][j] means finding the sum in matrix from (0,0) up to (i-1, j-1)
                # how to do this? take a 0-indexed 2x2 matrix as example (prefix_sum[2][2])
                # we can find this by adding row1 (0,0) to (0, 1): prefix_sum[1][2]
                # then add col1 (0,0) to (1, 0): prefix_sum[2][1]
                # add the (1,1) element: matrix[1][1]
                # delete the (0,0) that's repeated: prefix_sum
                # notice except for the (1,1) element, rest are really blocks. so they need prefix_sum representation
                self.prefix_sum[i][j] = self.prefix_sum[i-1][j] + self.prefix_sum[i][j-1] + matrix[i-1][j-1] - self.prefix_sum[i-1][j-1]


    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        # this is really the reverse operation now: to get the sum between the row1col1 block and row2col2 block:
        # use the row2col2(bigger) block - row1col2 block - row2col1 block + row1col1 block that's been deleted twice.
        # see image for better visualization
        return self.prefix_sum[row2+1][col2+1] - self.prefix_sum[row1][col2+1] - self.prefix_sum[row2+1][col1] + self.prefix_sum[row1][col1]
        # why not self.prefix_sum[row2+1][col2+1] - self.prefix_sum[row1+1][col2+1] - self.prefix_sum[row2+1][col1+1] + self.prefix_sum[row1+1][col1+1]
        # remember in 1d prefix sum sumregion, to find region between left and right it was prefix_sum[right+1] - self.prefix_sum[left]?
        # well, here to find region between row1col1 and row2col2, we had to use prefix_sum[row2+1][col2+1] as the area for matrix2, and prefix_sum[row1][col1] as matrix1,
        # plus deleting the horizontal and vertical remenants


# Solution 2
class NumMatrixSol2:
    def __init__(self, matrix: list[list[int]]):
        # TODO: write your second solution
        raise NotImplementedError("Implement NumMatrixSol2.__init__()")

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        raise NotImplementedError("Implement NumMatrixSol2.sumRegion()")


# Solution 3 (optional)
class NumMatrixSol3:
    def __init__(self, matrix: list[list[int]]):
        # TODO: write your third solution (optional)
        raise NotImplementedError("Implement NumMatrixSol3.__init__()")

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        raise NotImplementedError("Implement NumMatrixSol3.sumRegion()")


# =========================================
# Simple test function (major test cases)
# =========================================
def run_basic_tests(num_matrix_class) -> None:
    print(f"\nTesting: {num_matrix_class.__name__}")

    matrix = [
        [3, 0, 1, 4, 2],
        [5, 6, 3, 2, 1],
        [1, 2, 0, 1, 5],
        [4, 1, 0, 1, 7],
        [1, 0, 3, 0, 5],
    ]

    obj = num_matrix_class(matrix)
    r1 = obj.sumRegion(2, 1, 4, 3)  # 8
    r2 = obj.sumRegion(1, 1, 2, 2)  # 11
    r3 = obj.sumRegion(1, 2, 2, 4)  # 12

    got = [r1, r2, r3]
    expected = [8, 11, 12]

    if got == expected:
        print(f"PASS | got={got}")
    else:
        print(f"FAIL | got={got}, expected={expected}")


if __name__ == "__main__":
    run_basic_tests(NumMatrixSol1)
    # run_basic_tests(NumMatrixSol2)
    # run_basic_tests(NumMatrixSol3)



# =========================
# Notes (write here later)
# =========================
# - Key insight:
# - Time complexity notes:
# - Space complexity notes:
# - Common mistakes:
# - Follow-up ideas:
