"""
LeetCode 74 - Search a 2D Matrix
"""


def search_matrix_sol1(matrix: list[list[int]], target: int) -> bool:
    raise NotImplementedError("Implement search_matrix_sol1")


def search_matrix_sol2(matrix: list[list[int]], target: int) -> bool:
    raise NotImplementedError("Implement search_matrix_sol2")


def search_matrix_sol3(matrix: list[list[int]], target: int) -> bool:
    raise NotImplementedError("Implement search_matrix_sol3")


def run_basic_tests(solution_func) -> None:
    test_cases = [
        ([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 3, True),
        ([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 13, False),
        ([[1]], 1, True),
    ]
    print(f"\nTesting: {solution_func.__name__}")
    passed = 0
    for matrix, target, expected in test_cases:
        got = solution_func([row[:] for row in matrix], target)
        if got == expected:
            passed += 1
            print(f"PASS | target={target} -> {got}")
        else:
            print(f"FAIL | target={target} -> got {got}, expected {expected}")
    print(f"Passed {passed}/{len(test_cases)} test cases.")


if __name__ == "__main__":
    # run_basic_tests(search_matrix_sol1)
    # run_basic_tests(search_matrix_sol2)
    # run_basic_tests(search_matrix_sol3)
    pass
