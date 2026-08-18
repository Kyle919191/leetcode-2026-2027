"""
LeetCode 150 - Evaluate Reverse Polish Notation
"""


def eval_rpn_sol1(tokens: list[str]) -> int:
    stack = []
    expressions = ["+", "-", "*", "/"]
    for tok in tokens:
        if tok not in expressions:
            stack.append(int(tok))
            continue # skip this iteration
        b = stack.pop() # first pop is b! in the case of 35-, it should be 3-5, so assign 5 as b
        a = stack.pop()
        # TODO-TALK: For operators, pop right operand first, then left operand.
        if tok == "+":
            stack.append(a + b)
        elif tok == "-":
            stack.append(a - b)
        elif tok == "*":
            stack.append(a * b)
        else:
            stack.append(int(a / b))
    return stack[-1]



def eval_rpn_sol2(tokens: list[str]) -> int:
    raise NotImplementedError("Implement eval_rpn_sol2")


def eval_rpn_sol3(tokens: list[str]) -> int:
    raise NotImplementedError("Implement eval_rpn_sol3")


def run_basic_tests(solution_func) -> None:
    test_cases = [
        (["2", "1", "+", "3", "*"], 9),
        (["4", "13", "5", "/", "+"], 6),
        (["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"], 22),
    ]
    print(f"\nTesting: {solution_func.__name__}")
    passed = 0
    for tokens, expected in test_cases:
        got = solution_func(tokens[:])
        if got == expected:
            passed += 1
            print(f"PASS | tokens={tokens} -> {got}")
        else:
            print(f"FAIL | tokens={tokens} -> got {got}, expected {expected}")
    print(f"Passed {passed}/{len(test_cases)} test cases.")


if __name__ == "__main__":
    run_basic_tests(eval_rpn_sol1)
    # run_basic_tests(eval_rpn_sol2)
    # run_basic_tests(eval_rpn_sol3)
    pass
