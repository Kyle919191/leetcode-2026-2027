"""
LeetCode 424 - Longest Repeating Character Replacement
"""


def character_replacement_sol1(s: str, k: int) -> int:
    # TODO-TALK: I maintain a window and track the highest single-character count inside it.
    # TODO-TALK: The window is valid if window_size - max_count is at most k.
    # TODO-TALK: If invalid, I shrink from the left until it becomes valid again.
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
    raise NotImplementedError("Implement character_replacement_sol2")


def character_replacement_sol3(s: str, k: int) -> int:
    raise NotImplementedError("Implement character_replacement_sol3")


def run_basic_tests(solution_func) -> None:
    test_cases = [
        ("ABAB", 2, 4),
        ("AABABBA", 1, 4),
        ("AAAA", 2, 4),
    ]
    print(f"\nTesting: {solution_func.__name__}")
    passed = 0
    for s, k, expected in test_cases:
        got = solution_func(s, k)
        if got == expected:
            passed += 1
            print(f'PASS | s="{s}", k={k} -> {got}')
        else:
            print(f'FAIL | s="{s}", k={k} -> got {got}, expected {expected}')
    print(f"Passed {passed}/{len(test_cases)} test cases.")


if __name__ == "__main__":
    # run_basic_tests(character_replacement_sol1)
    # run_basic_tests(character_replacement_sol2)
    # run_basic_tests(character_replacement_sol3)
    pass
