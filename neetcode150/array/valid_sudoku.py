"""
LeetCode 36 - Valid Sudoku
"""


def is_valid_sudoku_sol1(board: list[list[str]]) -> bool:
    raise NotImplementedError("Implement is_valid_sudoku_sol1")


def is_valid_sudoku_sol2(board: list[list[str]]) -> bool:
    raise NotImplementedError("Implement is_valid_sudoku_sol2")


def is_valid_sudoku_sol3(board: list[list[str]]) -> bool:
    raise NotImplementedError("Implement is_valid_sudoku_sol3")


def run_basic_tests(solution_func) -> None:
    board_valid = [
        ["5", "3", ".", ".", "7", ".", ".", ".", "."],
        ["6", ".", ".", "1", "9", "5", ".", ".", "."],
        [".", "9", "8", ".", ".", ".", ".", "6", "."],
        ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
        ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
        ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
        [".", "6", ".", ".", ".", ".", "2", "8", "."],
        [".", ".", ".", "4", "1", "9", ".", ".", "5"],
        [".", ".", ".", ".", "8", ".", ".", "7", "9"],
    ]
    board_invalid = [row[:] for row in board_valid]
    board_invalid[0][0] = "8"
    test_cases = [(board_valid, True), (board_invalid, False)]
    print(f"\nTesting: {solution_func.__name__}")
    passed = 0
    for board, expected in test_cases:
        got = solution_func([r[:] for r in board])
        if got == expected:
            passed += 1
            print(f"PASS | expected {expected}")
        else:
            print(f"FAIL | got {got}, expected {expected}")
    print(f"Passed {passed}/{len(test_cases)} test cases.")


if __name__ == "__main__":
    # run_basic_tests(is_valid_sudoku_sol1)
    # run_basic_tests(is_valid_sudoku_sol2)
    # run_basic_tests(is_valid_sudoku_sol3)
    pass
