"""
LeetCode 242 - Valid Anagram

Task:
Given two strings `s` and `t`, return `True` if the two strings are anagrams of
each other. Otherwise, return `False`.

An anagram is a string that contains the exact same characters as another
string, but the order of the characters can be different.

Example 1:
Input: s = "racecar", t = "carrace"
Output: True

Example 2:
Input: s = "jar", t = "jam"
Output: False
"""


# Solution 1
def is_anagram_sol1(s: str, t: str) -> bool:
    # TODO: write your first solution
    raise NotImplementedError("Implement is_anagram_sol1")


# Solution 2
def is_anagram_sol2(s: str, t: str) -> bool:
    # TODO: write your second solution
    raise NotImplementedError("Implement is_anagram_sol2")


# Solution 3 (optional)
def is_anagram_sol3(s: str, t: str) -> bool:
    # TODO: write your third solution (optional)
    raise NotImplementedError("Implement is_anagram_sol3")


# =========================================
# Simple test function (major test cases)
# =========================================
def run_basic_tests(solution_func) -> None:
    test_cases = [
        ("racecar", "carrace", True),   # example true
        ("jar", "jam", False),          # example false
        ("", "", True),                 # empty strings
        ("a", "a", True),               # single-char equal
        ("a", "b", False),              # single-char different
        ("anagram", "nagaram", True),   # common true case
        ("rat", "car", False),          # common false case
        ("aacc", "ccac", False),        # different counts
        ("listen", "silent", True),     # reorder same chars
    ]

    print(f"\nTesting: {solution_func.__name__}")
    passed = 0

    for s, t, expected in test_cases:
        result = solution_func(s, t)
        if result == expected:
            passed += 1
            print(f'PASS | s="{s}", t="{t}" -> {result}')
        else:
            print(f'FAIL | s="{s}", t="{t}" -> got {result}, expected {expected}')

    print(f"Passed {passed}/{len(test_cases)} test cases.")


if __name__ == "__main__":
    run_basic_tests(is_anagram_sol1)
    run_basic_tests(is_anagram_sol2)
    run_basic_tests(is_anagram_sol3)
    pass


# =========================
# anagram character frequency
# =========================
