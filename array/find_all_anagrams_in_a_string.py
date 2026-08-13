"""
LeetCode 438 - Find All Anagrams in a String

Task:
Given two strings `s` and `p`, return an array of all the start indices of
`p`'s anagrams in `s`. You may return the answer in any order.

Example 1:
Input: s = "cbaebabacd", p = "abc"
Output: [0,6]

Example 2:
Input: s = "abab", p = "ab"
Output: [0,1,2]
"""


# Solution 1
# anagram is the same as permutation, so similar to permutation_in_string.py
def find_anagrams_sol1(s: str, p: str) -> list[int]:
    window = {} # again, whenever u need a valid check(anagram found), we need a window dict
    need = {}
    for elem in p:
        need[elem] = need.get(elem, 0) + 1
    
    left = right = valid = 0
    result = []

    while right < len(s):
        expanded = s[right]
        right += 1
        
        if expanded in need:
            window[expanded] = window.get(expanded, 0) + 1
            if window[expanded] == need[expanded]:
                valid += 1
        
        while right - left >= len(p):
            if valid == len(need):
                result.append(left) # again, this is valid because the window size is always equal to target anagram size except when anagram size(p) is 0
            
            shrinked = s[left]
            left += 1
            
            if shrinked in need:
                if window[shrinked] == need[shrinked]:
                    valid -= 1
                window[shrinked] -= 1
    return result

# Solution 2
def find_anagrams_sol2(s: str, p: str) -> list[int]:
    # TODO: write your second solution
    raise NotImplementedError("Implement find_anagrams_sol2")


# Solution 3 (optional)
def find_anagrams_sol3(s: str, p: str) -> list[int]:
    # TODO: write your third solution (optional)
    raise NotImplementedError("Implement find_anagrams_sol3")


# =========================================
# Simple test function (major test cases)
# =========================================
def run_basic_tests(solution_func) -> None:
    test_cases = [
        ("cbaebabacd", "abc", [0, 6]),
        ("abab", "ab", [0, 1, 2]),
        ("a", "a", [0]),
        ("a", "b", []),
        ("baa", "aa", [1]),
        ("aaaaaaaaaa", "aaaa", [0, 1, 2, 3, 4, 5, 6]),
    ]

    print(f"\nTesting: {solution_func.__name__}")
    passed = 0

    for s, p, expected in test_cases:
        result = solution_func(s, p)
        if result == expected:
            passed += 1
            print(f'PASS | s="{s}", p="{p}" -> {result}')
        else:
            print(f'FAIL | s="{s}", p="{p}" -> got {result}, expected {expected}')

    print(f"Passed {passed}/{len(test_cases)} test cases.")


if __name__ == "__main__":
    run_basic_tests(find_anagrams_sol1)
    # run_basic_tests(find_anagrams_sol2)
    # run_basic_tests(find_anagrams_sol3)



# =========================
# Notes (write here later)
# =========================
# - Key insight:
# - Time complexity notes:
# - Space complexity notes:
# - Common mistakes:
# - Follow-up ideas:
