"""
LeetCode 3 - Longest Substring Without Repeating Characters

Task:
Given a string `s`, find the length of the longest substring without repeating
characters.

Example 1:
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

Example 2:
Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

Example 3:
Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
"""


# Solution 1
def length_of_longest_substring_sol1(s: str) -> int:
    window = {}
    left = right = result = 0

    while right < len(s):
        expanded = s[right]
        right += 1
        window[expanded] = window.get(expanded, 0) + 1

        while window[expanded] > 1: #repeating shows up, need
            # 1)remove this repetition, so it can find the next substring
            # 2)record this valid length after repetition removed
            shrinked = s[left]
            left += 1
            window[shrinked] -= 1

        result = max(result, right - left)
    return result




# Solution 2
def length_of_longest_substring_sol2(s: str) -> int:
    # TODO: write your second solution
    raise NotImplementedError("Implement length_of_longest_substring_sol2")


# Solution 3 (optional)
def length_of_longest_substring_sol3(s: str) -> int:
    # TODO: write your third solution (optional)
    raise NotImplementedError("Implement length_of_longest_substring_sol3")


# =========================================
# Simple test function (major test cases)
# =========================================
def run_basic_tests(solution_func) -> None:
    test_cases = [
        ("abcabcbb", 3),
        ("bbbbb", 1),
        ("pwwkew", 3),
        ("", 0),
        ("au", 2),
        ("dvdf", 3),
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
    run_basic_tests(length_of_longest_substring_sol1)
    # run_basic_tests(length_of_longest_substring_sol2)
    # run_basic_tests(length_of_longest_substring_sol3)



# =========================
# Notes (write here later)
# =========================
# - Key insight:
# - Time complexity notes:
# - Space complexity notes:
# - Common mistakes:
# - Follow-up ideas:
