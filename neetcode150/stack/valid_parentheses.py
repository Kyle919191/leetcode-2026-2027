"""
LeetCode 20 - Valid Parentheses
"""


def is_valid_sol1(s: str) -> bool:
    pairs = {')': '(', ']': '[', '}': '{'}
    stack = []
    for ch in s:
        if ch in pairs:
            # TODO-TALK: Closing bracket must match the latest opening bracket.
            if not stack or stack[-1] != pairs[ch]: # imitate stack behavior, check latest non-matched open parenthese
                # idea: A closing bracket must match the most recent unmatched opening bracket.
                # check not stack because if there are no open parathesis right now and there's a closed coming in, it's definitely wrong
                return False
            stack.pop() # if match, remove that opening parenthesis
        else:
             # TODO-TALK: Opening bracket waits for a future match.
            stack.append(ch)
    return len(stack) == 0


def is_valid_sol2(s: str) -> bool:
    raise NotImplementedError("Implement is_valid_sol2")


def is_valid_sol3(s: str) -> bool:
    raise NotImplementedError("Implement is_valid_sol3")


def run_basic_tests(solution_func) -> None:
    test_cases = [
        ("()", True),
        ("()[]{}", True),
        ("(]", False),
        ("([)]", False),
        ("{[]}", True),
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
    run_basic_tests(is_valid_sol1)
    # run_basic_tests(is_valid_sol2)
    # run_basic_tests(is_valid_sol3)

