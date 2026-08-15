"""
LeetCode 395 - Longest Substring with At Least K Repeating Characters

Task:
Given a string `s` and an integer `k`, return the length of the longest
substring of `s` such that the frequency of each character in this substring is
greater than or equal to `k`.

Example 1:
Input: s = "aaabb", k = 3
Output: 3

Example 2:
Input: s = "ababbc", k = 2
Output: 5
"""

def longestKLetterSubstr(s: str, k: int, count: int) -> int:
    left = right = 0
    max_len = 0 # this is the base case(length 0) instead of -infinity
    unique_count = 0
    valid_count = 0
    window = {}


    while right < len(s):
        elem = s[right]
        

        # at each expansion/shrink, update unique and valid, and window
        if elem not in window:
            unique_count += 1
        
        window[elem] = window.get(elem, 0) + 1 # this must go before valid check

        if window[elem] == k:
            valid_count += 1
        
        right += 1 

        while unique_count > count:
            letter = s[left]

            if window[letter] == k: # valid check in shrink must go before shrink
                valid_count -= 1
            
            window[letter] -= 1

            if window[letter] == 0:
                unique_count -= 1
                del window[letter]
            
            left += 1
        
        # we have to explicitly check for if the window is now valid. we have to check valid_count == count, unique count check can be ignored cuz we checked before shrink
        if unique_count == count and valid_count == count: # we have unique_count number of distinct letters, each valid
            max_len = max(max_len, right - left)
    
    return max_len




# Solution 1
# traditional sliding window doesn't work here, because:
# For example, the frequency of some characters in the window may not meet k, but it might be satisfied by expanding the window further. 
# But if you say that, then you might as well keep expanding the window, so you can't be sure when you should shrink the window.
# however, we can still use sliding window with an modification
def longest_substring_k_repeat_sol1(s: str, k: int) -> int:
    length = 0
    for i in range(1, 27): # 26 letters, so at most we can have 26 distinct letters in the array
        length = max(length, longestKLetterSubstr(s, k, i))
    return length



# Solution 2
def longest_substring_k_repeat_sol2(s: str, k: int) -> int:
    # TODO: write your second solution
    raise NotImplementedError("Implement longest_substring_k_repeat_sol2")


# Solution 3 (optional)
def longest_substring_k_repeat_sol3(s: str, k: int) -> int:
    # TODO: write your third solution (optional)
    raise NotImplementedError("Implement longest_substring_k_repeat_sol3")


# =========================================
# Simple test function (major test cases)
# =========================================
def run_basic_tests(solution_func) -> None:
    test_cases = [
        ("aaabb", 3, 3),
        ("ababbc", 2, 5),
        ("weitong", 2, 0),
        ("aaa", 1, 3),
        ("", 1, 0),
        ("aaabbb", 3, 6),
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
    run_basic_tests(longest_substring_k_repeat_sol1)
    # run_basic_tests(longest_substring_k_repeat_sol2)
    # run_basic_tests(longest_substring_k_repeat_sol3)



# =========================
# Notes (write here later)
# =========================
# - Key insight:
# - Time complexity notes:
# - Space complexity notes:
# - Common mistakes:
# - Follow-up ideas:
