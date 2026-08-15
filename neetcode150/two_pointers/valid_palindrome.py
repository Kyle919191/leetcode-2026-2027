"""
LeetCode 125 - Valid Palindrome
"""


def is_palindrome_sol1(s: str) -> bool:
    # TODO-TALK: I will keep only alphanumeric characters and lowercase them first.
    # TODO-TALK: Then I can compare from both ends and stop on the first mismatch.
    cleaned = []
    for elem in s:
        if elem.isalnum(): # alphanumeric, exclude spaces, colons, etc
            cleaned.append(elem.lower())
    
    left, right = 0, len(cleaned) - 1
    # TODO-TALK: Every step compares mirrored characters, then moves inward.
    while left < right: #left=right guanratees to work, so meaningless
        if cleaned[left] != cleaned[right]:
            return False
        left += 1
        right -= 1
    return True


# Solution 2


def is_palindrome_sol2(s: str) -> bool:
    raise NotImplementedError("Implement is_palindrome_sol2")


def is_palindrome_sol3(s: str) -> bool:
    raise NotImplementedError("Implement is_palindrome_sol3")


def run_basic_tests(solution_func) -> None:
    test_cases = [
        ("A man, a plan, a canal: Panama", True),
        ("race a car", False),
        (" ", True),
        ("0P", False),
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
    # run_basic_tests(is_palindrome_sol1)
    # run_basic_tests(is_palindrome_sol2)
    # run_basic_tests(is_palindrome_sol3)
    pass
