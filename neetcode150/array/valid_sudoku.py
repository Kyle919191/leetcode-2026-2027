"""
LeetCode 36 - Valid Sudoku
"""

# for block, we're definint 9 blocks like:
# block0 block1 block2
# block3 block4 block5 ...
def is_valid_sudoku_sol1(board: list[list[str]]) -> bool:
    rows = [set() for _ in range(9)] # 9 sets, one set for one row
    cols = [set() for _ in range(9)]
    block = [set() for _ in range(9)]

    for r in range(9):
        for c in range(9):
            value = board[r][c]
            if value == '.': # handle the case when it's empty
                continue
            b = r // 3 * 3 + c // 3 # calculate which block does this element fall in
            # TODO-TALK: Any repeat in row, column, or box makes board invalid.
            if value in rows[r] or value in cols[c] or value in block[b]:
                return False
            # TODO-TALK: Otherwise I record this digit in all three trackers.
            rows[r].add(value)
            cols[c].add(value)
            block[b].add(value)
    return True


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
    run_basic_tests(is_valid_sudoku_sol1)
    # run_basic_tests(is_valid_sudoku_sol2)
    # run_basic_tests(is_valid_sudoku_sol3)

