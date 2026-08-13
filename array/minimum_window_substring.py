"""
LeetCode 76 - Minimum Window Substring

Task:
Given two strings `s` and `t` of lengths `m` and `n` respectively, return the
minimum window substring of `s` such that every character in `t` (including
duplicates) is included in the window.

If there is no such substring, return the empty string `""`.

Example 1:
Input: s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"

Example 2:
Input: s = "a", t = "a"
Output: "a"

Example 3:
Input: s = "a", t = "aa"
Output: ""
"""


# Solution 1
def min_window_sol1(s: str, t: str) -> str:
    window = {}
    need = {}
    for element in t:
        need[element] = need.get(element, 0) + 1
    
    left = right = valid = 0
    
    start = 0
    length = float('inf')
    while right < len(s):
        expanded = s[right]
        right += 1
        if expanded in need:
            window[expanded] = window.get(expanded, 0) + 1 # note that it's possible for window[expanded] > need[expanded] later
            if window[expanded] == need[expanded]:
                valid += 1

        while valid == len(need): # one valid means window has at least as much copies of one element as need
            # this now marks the point where we have enough of all need, which means right now this substring between left and right is valid
            if (right - left) < length:
                start = left 
                length = right - left #recording our global best start and length
            
            shrinked = s[left]
            left += 1

            if shrinked in need: # if d in need, then d will also already have an entry in window
                if window[shrinked] == need[shrinked]:
                    valid -= 1
                window[shrinked] -= 1 # in expansion, we need to first increment then check for valid, in shrink we first check for valid then decrement
    
    return "" if length == float('inf') else s[start: start+length]    




# Solution 2
def min_window_sol2(s: str, t: str) -> str:
    # TODO: write your second solution
    raise NotImplementedError("Implement min_window_sol2")


# Solution 3 (optional)
def min_window_sol3(s: str, t: str) -> str:
    # TODO: write your third solution (optional)
    raise NotImplementedError("Implement min_window_sol3")


# =========================================
# Simple test function (major test cases)
# =========================================
def run_basic_tests(solution_func) -> None:
    test_cases = [
        ("ADOBECODEBANC", "ABC", "BANC"),
        ("a", "a", "a"),
        ("a", "aa", ""),
        ("aa", "aa", "aa"),
        ("ab", "A", ""),
        ("bba", "ab", "ba"),
    ]

    print(f"\nTesting: {solution_func.__name__}")
    passed = 0

    for s, t, expected in test_cases:
        result = solution_func(s, t)
        if result == expected:
            passed += 1
            print(f'PASS | s="{s}", t="{t}" -> "{result}"')
        else:
            print(
                f'FAIL | s="{s}", t="{t}" -> got "{result}", expected "{expected}"'
            )

    print(f"Passed {passed}/{len(test_cases)} test cases.")


if __name__ == "__main__":
    run_basic_tests(min_window_sol1)
    # run_basic_tests(min_window_sol2)
    # run_basic_tests(min_window_sol3)


# =========================
# Notes (write here later)
# =========================
# - Key insight:
# - Time complexity notes:
# - Space complexity notes:
# - Common mistakes:
# - Follow-up ideas:
