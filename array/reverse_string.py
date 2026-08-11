"""
LeetCode 344 - Reverse String

Task:
Write a function that reverses a string. The input string is given as an array
of characters `s`.

You must do this by modifying the input array in-place with O(1) extra memory.

Example 1:
Input: s = ["h","e","l","l","o"]
Output: ["o","l","l","e","h"]

Example 2:
Input: s = ["H","a","n","n","a","h"]
Output: ["h","a","n","n","a","H"]
"""


# Solution 1
def reverse_string_sol1(s: list[str]) -> None:
    left = 0
    right = len(s)-1
    while left < right: #left <= right also works
        temp = s[left]
        s[left] = s[right]
        s[right] = temp
        left += 1
        right -= 1
    return s


# Solution 2
def reverse_string_sol2(s: list[str]) -> None:
    # TODO: write your second solution
    raise NotImplementedError("Implement reverse_string_sol2")


# Solution 3 (optional)
def reverse_string_sol3(s: list[str]) -> None:
    # TODO: write your third solution (optional)
    raise NotImplementedError("Implement reverse_string_sol3")


# =========================================
# Simple test function (major test cases)
# =========================================
def run_basic_tests(solution_func) -> None:
    test_cases = [
        (["h", "e", "l", "l", "o"], ["o", "l", "l", "e", "h"]),
        (["H", "a", "n", "n", "a", "h"], ["h", "a", "n", "n", "a", "H"]),
        (["a"], ["a"]),
        ([], []),
        (["1", "2", "3", "4"], ["4", "3", "2", "1"]),
    ]

    print(f"\nTesting: {solution_func.__name__}")
    passed = 0

    for s, expected in test_cases:
        arr = s[:]
        solution_func(arr)
        if arr == expected:
            passed += 1
            print(f"PASS | s={s} -> {arr}")
        else:
            print(f"FAIL | s={s} -> got {arr}, expected {expected}")

    print(f"Passed {passed}/{len(test_cases)} test cases.")


if __name__ == "__main__":
    run_basic_tests(reverse_string_sol1)
    # run_basic_tests(reverse_string_sol2)
    # run_basic_tests(reverse_string_sol3)



# =========================
# Notes (write here later)
# =========================
# - Key insight:
# - Time complexity notes:
# - Space complexity notes:
# - Common mistakes:
# - Follow-up ideas:
