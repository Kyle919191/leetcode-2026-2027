"""
LeetCode 242 - Valid Anagram
"""


def is_anagram_sol1(s: str, t: str) -> bool:
    freq = {}
    if len(s) != len(t): # not equal length case
        return False
    for elem in s:
        freq[elem] = freq.get(elem, 0) + 1
    for elem in t:
        if elem not in freq: # not the same characters case
            return False
        freq[elem] -= 1
        if freq[elem] < 0: # elem frequency mismatch case
            return False
    return True




def is_anagram_sol2(s: str, t: str) -> bool:
    raise NotImplementedError("Implement is_anagram_sol2")


def is_anagram_sol3(s: str, t: str) -> bool:
    raise NotImplementedError("Implement is_anagram_sol3")


def run_basic_tests(solution_func) -> None:
    test_cases = [
        ("anagram", "nagaram", True),
        ("rat", "car", False),
        ("", "", True),
        ("aacc", "ccac", False),
    ]
    print(f"\nTesting: {solution_func.__name__}")
    passed = 0
    for s, t, expected in test_cases:
        got = solution_func(s, t)
        if got == expected:
            passed += 1
            print(f'PASS | s="{s}", t="{t}" -> {got}')
        else:
            print(f'FAIL | s="{s}", t="{t}" -> got {got}, expected {expected}')
    print(f"Passed {passed}/{len(test_cases)} test cases.")


if __name__ == "__main__":
    run_basic_tests(is_anagram_sol1)
    # run_basic_tests(is_anagram_sol2)
    # run_basic_tests(is_anagram_sol3)

