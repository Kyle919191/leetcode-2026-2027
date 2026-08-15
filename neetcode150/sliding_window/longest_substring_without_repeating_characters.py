"""
LeetCode 3 - Longest Substring Without Repeating Characters
"""


def length_of_longest_substring_sol1(s: str) -> int:
    window = {}
    left = right = result = 0

    while right < len(s):
        expanded = s[right]
        right += 1
        # TODO-TALK: I expand the window by including this character.
        window[expanded] = window.get(expanded, 0) + 1

        while window[expanded] > 1: #repeating shows up, need
            # 1)remove this repetition, so it can find the next substring
            # 2)record this valid length after repetition removed
            # TODO-TALK: This character now repeats, so I shrink from left until it is unique again.
            shrinked = s[left]
            left += 1
            window[shrinked] -= 1

        # TODO-TALK: At this point window has no repeats, so I update the best length.
        result = max(result, right - left)
    return result


def length_of_longest_substring_sol2(s: str) -> int:
    raise NotImplementedError("Implement length_of_longest_substring_sol2")


def length_of_longest_substring_sol3(s: str) -> int:
    raise NotImplementedError("Implement length_of_longest_substring_sol3")


def run_basic_tests(solution_func) -> None:
    test_cases = [
        ("abcabcbb", 3),
        ("bbbbb", 1),
        ("pwwkew", 3),
        ("", 0),
    ]
    print(f"\nTesting: {solution_func.__name__}")
    passed = 0
    for s, expected in test_cases:
        got = solution_func(s)
        if got == expected:
            passed += 1
            print(f'PASS | s="{s}" -> {got}')
        else:
            print(f'FAIL | s="{s}" -> got {got}, expected {expected}')
    print(f"Passed {passed}/{len(test_cases)} test cases.")


if __name__ == "__main__":
    # run_basic_tests(length_of_longest_substring_sol1)
    # run_basic_tests(length_of_longest_substring_sol2)
    # run_basic_tests(length_of_longest_substring_sol3)
    pass
