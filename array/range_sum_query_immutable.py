"""
LeetCode 303 - Range Sum Query - Immutable

Task:
Given an integer array `nums`, handle multiple queries of the following type:

- Calculate the sum of the elements of `nums` between indices `left` and
  `right` inclusive, where `left <= right`.

Implement the `NumArray` class:
- `NumArray(nums)` initializes the object with the integer array `nums`.
- `sumRange(left, right)` returns the sum of the elements of `nums` between
  indices `left` and `right` inclusive.

Example:
Input:
["NumArray", "sumRange", "sumRange", "sumRange"]
[[[-2, 0, 3, -5, 2, -1]], [0, 2], [2, 5], [0, 5]]
Output:
[null, 1, -1, -3]
"""


# Solution 1
class NumArraySol1:
    # in init, build the prefix sum array
    def __init__(self, nums: list[int]):
        # prefix sum length is one more than nums because we need:
        # preSum[0] = 0, to facilitate the calculation of accumulated sums
        self.prefix_sum = [0] * (len(nums) + 1) 
        for i in range(1, len(self.prefix_sum)): # start from idx 1, because preSum[0] is 0 already
            self.prefix_sum[i] = self.prefix_sum[i-1] + nums[i-1] # nums i - 1 because prefix sum is one length more tha sum,
            # this means that prefix_sum[3] means the sum of nums[0] to nums[2]

    def sumRange(self, left: int, right: int) -> int:
        return self.prefix_sum[right+1] - self.prefix_sum[left] # see image in array/ for more context
        # in short: say we want nums[1] to nums[4]. prefix_sum[5] gets us nums[0] to nums[4], with nums[4] inclusive
        # we then want to remove nums[0], which is done by prefix[1]


# Solution 2
class NumArraySol2:
    def __init__(self, nums: list[int]):
        # TODO: write your second solution
        raise NotImplementedError("Implement NumArraySol2.__init__()")

    def sumRange(self, left: int, right: int) -> int:
        raise NotImplementedError("Implement NumArraySol2.sumRange()")


# Solution 3 (optional)
class NumArraySol3:
    def __init__(self, nums: list[int]):
        # TODO: write your third solution (optional)
        raise NotImplementedError("Implement NumArraySol3.__init__()")

    def sumRange(self, left: int, right: int) -> int:
        raise NotImplementedError("Implement NumArraySol3.sumRange()")


# =========================================
# Simple test function (major test cases)
# =========================================
def run_basic_tests(num_array_class) -> None:
    print(f"\nTesting: {num_array_class.__name__}")

    obj = num_array_class([-2, 0, 3, -5, 2, -1])
    r1 = obj.sumRange(0, 2)  # 1
    r2 = obj.sumRange(2, 5)  # -1
    r3 = obj.sumRange(0, 5)  # -3

    got = [r1, r2, r3]
    expected = [1, -1, -3]

    if got == expected:
        print(f"PASS | got={got}")
    else:
        print(f"FAIL | got={got}, expected={expected}")


if __name__ == "__main__":
    run_basic_tests(NumArraySol1)
    # run_basic_tests(NumArraySol2)
    # run_basic_tests(NumArraySol3)


# =========================
# Notes (write here later)
# =========================
# - Key insight:
# - Time complexity notes:
# - Space complexity notes:
# - Common mistakes:
# - Follow-up ideas:
