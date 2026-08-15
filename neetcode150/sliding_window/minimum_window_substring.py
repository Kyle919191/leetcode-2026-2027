"""
LeetCode 76 - Minimum Window Substring
"""


def min_window_sol1(s: str, t: str) -> str:
    window = {}
    need = {}
    for element in t:
        # TODO-TALK: I first build the required counts for every character in t.
        need[element] = need.get(element, 0) + 1
    
    left = right = valid = 0
    
    start = 0
    length = float('inf')
    while right < len(s):
        expanded = s[right]
        right += 1
        if expanded in need:
            # TODO-TALK: I only update counts for characters that are part of the target.
            window[expanded] = window.get(expanded, 0) + 1 # note that it's possible for window[expanded] > need[expanded] later
            if window[expanded] == need[expanded]:
                valid += 1

        while valid == len(need): # one valid means window has at least as much copies of one element as need
            # this now marks the point where we have enough of all need, which means right now this substring between left and right is valid
            if (right - left) < length:
                # TODO-TALK: This window is valid and smaller, so I store it as current best answer.
                start = left 
                length = right - left #recording our global best start and length
            
            shrinked = s[left]
            left += 1

            if shrinked in need: # if d in need, then d will also already have an entry in window
                # TODO-TALK: Before reducing count, I check whether this char was satisfying a need exactly.
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
