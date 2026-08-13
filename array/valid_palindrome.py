"""
LeetCode 125 - Valid Palindrome

Task:
A phrase is a palindrome if, after converting all uppercase letters into
lowercase letters and removing all non-alphanumeric characters, it reads the
same forward and backward.

Given a string `s`, return `True` if it is a palindrome, or `False` otherwise.

Example 1:
Input: s = "A man, a plan, a canal: Panama"
Output: True

Example 2:
Input: s = "race a car"
Output: False

Example 3:
Input: s = " "
Output: True
"""

#similar to linked_list/palindrome_linked_list.py(234) but now for non-linkedlist string with spaces

# Solution 1
def is_palindrome_sol1(s: str) -> bool:
    cleaned = []
    for elem in s:
        if elem.isalnum(): # alphanumeric, exclude spaces, colons, etc
            cleaned.append(elem.lower())
    
    left, right = 0, len(cleaned) - 1
    while left < right: #left=right guanratees to work, so meaningless
        if cleaned[left] != cleaned[right]:
            return False
        left += 1
        right -= 1
    return True


# Solution 2
def is_palindrome_sol2(s: str) -> bool:
    # TODO: write your second solution
    raise NotImplementedError("Implement is_palindrome_sol2")


# Solution 3 (optional)
def is_palindrome_sol3(s: str) -> bool:
    # TODO: write your third solution (optional)
    raise NotImplementedError("Implement is_palindrome_sol3")


# =========================================
# Simple test function (major test cases)
# =========================================
def run_basic_tests(solution_func) -> None:
    test_cases = [
        ("A man, a plan, a canal: Panama", True),
        ("race a car", False),
        (" ", True),
        ("0P", False),
        ("abba", True),
        ("ab_a", True),
        ("No 'x' in Nixon", True),
        (".,", True),
    ]

    print(f"\nTesting: {solution_func.__name__}")
    passed = 0

    for s, expected in test_cases:
        result = solution_func(s)
        if result == expected:
            passed += 1
            print(f'PASS | s="{s}" -> {result}')
        else:
            print(f'FAIL | s="{s}" -> got {result}, expected {expected}')

    print(f"Passed {passed}/{len(test_cases)} test cases.")


if __name__ == "__main__":
    run_basic_tests(is_palindrome_sol1)
    # run_basic_tests(is_palindrome_sol2)
    # run_basic_tests(is_palindrome_sol3)


# =========================
# Notes (write here later)
# =========================
# - Key insight:
# - Time complexity notes:
# - Space complexity notes:
# - Common mistakes:
# - Follow-up ideas:
