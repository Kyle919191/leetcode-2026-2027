"""
LeetCode 76 - Minimum Window Substring
"""


def min_window_sol1(s: str, t: str) -> str:
    # TODO-TALK: I expand right until the window covers all required counts from t.
    # TODO-TALK: Once valid, I shrink left to find the smallest valid window for that right edge.
    # TODO-TALK: I keep the global best start and length across all valid windows.
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
    raise NotImplementedError("Implement min_window_sol2")


def min_window_sol3(s: str, t: str) -> str:
    raise NotImplementedError("Implement min_window_sol3")


def run_basic_tests(solution_func) -> None:
    test_cases = [
        ("ADOBECODEBANC", "ABC", "BANC"),
        ("a", "a", "a"),
        ("a", "aa", ""),
    ]
    print(f"\nTesting: {solution_func.__name__}")
    passed = 0
    for s, t, expected in test_cases:
        got = solution_func(s, t)
        if got == expected:
            passed += 1
            print(f'PASS | s="{s}", t="{t}" -> "{got}"')
        else:
            print(f'FAIL | s="{s}", t="{t}" -> got "{got}", expected "{expected}"')
    print(f"Passed {passed}/{len(test_cases)} test cases.")


if __name__ == "__main__":
    # run_basic_tests(min_window_sol1)
    # run_basic_tests(min_window_sol2)
    # run_basic_tests(min_window_sol3)
    pass
