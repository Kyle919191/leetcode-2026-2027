"""
LeetCode 125 - Valid Palindrome
"""


def is_palindrome_sol1(s: str) -> bool:
    cleaned = []
    for elem in s:
        # TODO-TALK: I only keep letters and digits, and I lowercase so case does not matter.
        if elem.isalnum(): # alphanumeric, exclude spaces, colons, etc
            cleaned.append(elem.lower())
    
    left, right = 0, len(cleaned) - 1
    while left < right: #left=right guanratees to work, so meaningless
        # TODO-TALK: If mirrored characters differ, I can conclude it is not a palindrome.
        if cleaned[left] != cleaned[right]:
            return False
        # TODO-TALK: If they match, I move both pointers inward and continue.
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
