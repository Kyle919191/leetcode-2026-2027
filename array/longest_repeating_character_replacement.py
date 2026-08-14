"""
LeetCode 424 - Longest Repeating Character Replacement

Task:
You are given a string `s` and an integer `k`. You can choose any character of
the string and change it to any other uppercase English character. You can
perform this operation at most `k` times.

Return the length of the longest substring containing the same letter you can
get after performing the above operations.

Example 1:
Input: s = "ABAB", k = 2
Output: 4

Example 2:
Input: s = "AABABBA", k = 1
Output: 4
"""


# Solution 1
# similar to max_consecutive_ones_iii
# NOTE: the windowMaxCount may face staleness issue after shrinking. but thats fine because
# instead of being the maximum count in the current window it's more like the largest character count we've reached while expanding windows so far
def character_replacement_sol1(s: str, k: int) -> int:
    left = right = 0
    windowCharCount = [0] * 26 # use array instead of dict for easier access. We can do this because we convert alphabets to numbers via ord
    windowMaxCount = 0
    result = 0

    while right < len(s):
        c = ord(s[right]) - ord('A')
        windowCharCount[c] += 1
        windowMaxCount = max(windowMaxCount, windowCharCount[c])
        right += 1

        # can be switched to an if condition. this would really happen only once
        while (right - left - windowMaxCount) > k: # just like consecutiveones condition
            windowCharCount[ord(s[left]) - ord('A')] -= 1
            left += 1
        
         # now we have a valid window: calculate length
        result = max(result, right - left)
    
    return result

        


# Solution 2
def character_replacement_sol2(s: str, k: int) -> int:
    # TODO: write your second solution
    raise NotImplementedError("Implement character_replacement_sol2")


# Solution 3 (optional)
def character_replacement_sol3(s: str, k: int) -> int:
    # TODO: write your third solution (optional)
    raise NotImplementedError("Implement character_replacement_sol3")


# =========================================
# Simple test function (major test cases)
# =========================================
def run_basic_tests(solution_func) -> None:
    test_cases = [
        ("ABAB", 2, 4),
        ("AABABBA", 1, 4),
        ("AAAA", 2, 4),
        ("ABCDE", 1, 2),
        ("BAAAB", 2, 5),
        ("A", 0, 1),
    ]

    print(f"\nTesting: {solution_func.__name__}")
    passed = 0

    for s, k, expected in test_cases:
        result = solution_func(s, k)
        if result == expected:
            passed += 1
            print(f'PASS | s="{s}", k={k} -> {result}')
        else:
            print(f'FAIL | s="{s}", k={k} -> got {result}, expected {expected}')

    print(f"Passed {passed}/{len(test_cases)} test cases.")


if __name__ == "__main__":
    run_basic_tests(character_replacement_sol1)
    # run_basic_tests(character_replacement_sol2)
    # run_basic_tests(character_replacement_sol3)



# =========================
# Notes (write here later)
# =========================
# - Key insight:
# - Time complexity notes:
# - Space complexity notes:
# - Common mistakes:
# - Follow-up ideas:
