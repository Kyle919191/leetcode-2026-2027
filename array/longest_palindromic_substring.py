"""
LeetCode 5 - Longest Palindromic Substring

Task:
Given a string `s`, return the longest palindromic substring in `s`.

A string is palindromic if it reads the same forward and backward.

Example 1:
Input: s = "babad"
Output: "bab"
Note: "aba" is also a valid answer.

Example 2:
Input: s = "cbbd"
Output: "bb"
"""

def palindrome_helper(s: str, l: int, r: int) -> str:
    # think of this as starting from the middle and expand to left and right to find palindrome
    # if odd, l and r start at the same; if even, l and r are adjacent
    while l >= 0 and r < len(s) and s[l] == s[r]:
        l -= 1
        r += 1

    # while loop breaks meaning s[l+1..r-1] is the longest palindrome string(prev iteration)
    # so s[l + 1: r] is longest palindrome because RHS is exclusive
    return s[l + 1: r]

# Solution 1
def longest_palindrome_sol1(s: str) -> str:
    result = ""
    for i in range(len(s)):
        # CRITICAL: palindrome can be either odd length or even length
        # therefore, we check the longest possible EVEN and ODD palindrome that's centered at each index
        result1 = palindrome_helper(s, i, i)
        result2 = palindrome_helper(s, i, i+1)
        result = result if len(result) > len(result1) else result1
        result = result if len(result) > len(result2) else result2
    return result




# Solution 2
def longest_palindrome_sol2(s: str) -> str:
    # TODO: write your second solution
    raise NotImplementedError("Implement longest_palindrome_sol2")


# Solution 3 (optional)
def longest_palindrome_sol3(s: str) -> str:
    # TODO: write your third solution (optional)
    raise NotImplementedError("Implement longest_palindrome_sol3")


# =========================================
# Simple test function (major test cases)
# =========================================
def run_basic_tests(solution_func) -> None:
    test_cases = [
        ("babad", {"bab", "aba"}),  # both are accepted by LeetCode
        ("cbbd", {"bb"}),
        ("a", {"a"}),
        ("ac", {"a", "c"}),
        ("forgeeksskeegfor", {"geeksskeeg"}),
        ("aaaa", {"aaaa"}),
    ]

    print(f"\nTesting: {solution_func.__name__}")
    passed = 0

    for s, expected_set in test_cases:
        result = solution_func(s)
        if result in expected_set:
            passed += 1
            print(f'PASS | s="{s}" -> "{result}"')
        else:
            print(
                f'FAIL | s="{s}" -> got "{result}", '
                f"expected one of {sorted(expected_set)}"
            )

    print(f"Passed {passed}/{len(test_cases)} test cases.")


if __name__ == "__main__":
    run_basic_tests(longest_palindrome_sol1)
    # run_basic_tests(longest_palindrome_sol2)
    # run_basic_tests(longest_palindrome_sol3)



# =========================
# Notes (write here later)
# =========================
# - Key insight:
# - Time complexity notes:
# - Space complexity notes:
# - Common mistakes:
# - Follow-up ideas:
