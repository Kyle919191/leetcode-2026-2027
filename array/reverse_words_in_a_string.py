"""
LeetCode 151 - Reverse Words in a String

Task:
Given an input string `s`, reverse the order of the words.

A word is defined as a sequence of non-space characters. The words in `s` will
be separated by at least one space.

Return a string of the words in reverse order concatenated by a single space.
Note that `s` may contain leading/trailing spaces or multiple spaces between
two words. The returned string should only have a single space separating words
and no leading/trailing spaces.

Example 1:
Input: s = "the sky is blue"
Output: "blue is sky the"

Example 2:
Input: s = "  hello world  "
Output: "world hello"

Example 3:
Input: s = "a good   example"
Output: "example good a"
"""


# Solution 1
def reverse_words_sol1(s: str) -> str:
    words = s.split() # handle trailing spaces
    left, right = 0, len(words)-1

    while left < right:
        temp = words[left]
        words[left]  = words[right]
        words[right] = temp
        left += 1
        right -= 1
    
    return " ".join(words) 
    # alternative idea similar to linked_list/rotate_list.py:
    # first rotate the entire string, then reverse each word again



# Solution 2
def reverse_words_sol2(s: str) -> str:
    # TODO: write your second solution
    raise NotImplementedError("Implement reverse_words_sol2")


# Solution 3 (optional)
def reverse_words_sol3(s: str) -> str:
    # TODO: write your third solution (optional)
    raise NotImplementedError("Implement reverse_words_sol3")


# =========================================
# Simple test function (major test cases)
# =========================================
def run_basic_tests(solution_func) -> None:
    test_cases = [
        ("the sky is blue", "blue is sky the"),
        ("  hello world  ", "world hello"),
        ("a good   example", "example good a"),
        ("a", "a"),
        ("    ", ""),
    ]

    print(f"\nTesting: {solution_func.__name__}")
    passed = 0

    for s, expected in test_cases:
        result = solution_func(s)
        if result == expected:
            passed += 1
            print(f'PASS | s="{s}" -> "{result}"')
        else:
            print(f'FAIL | s="{s}" -> got "{result}", expected "{expected}"')

    print(f"Passed {passed}/{len(test_cases)} test cases.")


if __name__ == "__main__":
    run_basic_tests(reverse_words_sol1)
    # run_basic_tests(reverse_words_sol2)
    # run_basic_tests(reverse_words_sol3)



# =========================
# Notes (write here later)
# =========================
# - Key insight:
# - Time complexity notes:
# - Space complexity notes:
# - Common mistakes:
# - Follow-up ideas:
