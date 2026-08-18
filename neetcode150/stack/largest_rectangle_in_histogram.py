"""
LeetCode 84 - Largest Rectangle in Histogram
"""


def largest_rectangle_area_sol1(heights: list[int]) -> int:
    stack = [] # (start_index, height)
    best = 0
    for index, height in enumerate(heights):
        start = index # in monotonic case, start is just whatever current index
        # stack always contains monotonically increasing height
        # height is less than previous, meaning we've reached a drop; this means
        # Every taller bar on the stack has just found its right boundary, so we pop those taller bars and calculate their maximum possible rectangles
        while stack and stack[-1][1] > height:
            i, h = stack.pop()
            # case A.tall
            area = h * (index - i)
            best = max(best, area)
            start = i # start will eventually be the i such that index-i range all > height
        # case A.wide, which will be taken care later as either caseB.wide if it hits len(heights) or caseA.tall if it proceeds to see something smaller
        stack.append((start, height)) # when we hit this drop, this drop can go all the way back until there's something lower than drop
    
    # now there are still bars in the stack and they were never blocked by a shorter bar on their right
    # this means they can extend all the way to the end
    n = len(heights)
    while stack:
        i, h = stack.pop()
        # case B.wide + case B.tall
        area = h * (n-i) # their right boundary is no longer the index, but n
        best = max(best, area)
    # NOTE: takeaway: take a two bar example. there are two cases: left short right tall(25) or left tall right short(52).
    # in case A, there are two areas: 5x1 and 2x2. same for case B.
    return best




def largest_rectangle_area_sol2(heights: list[int]) -> int:#
    raise NotImplementedError("Implement largest_rectangle_area_sol2")


def largest_rectangle_area_sol3(heights: list[int]) -> int:
    raise NotImplementedError("Implement largest_rectangle_area_sol3")


def run_basic_tests(solution_func) -> None:
    test_cases = [
        ([2, 1, 5, 6, 2, 3], 10),
        ([2, 4], 4),
        ([2, 1, 2], 3),
    ]
    print(f"\nTesting: {solution_func.__name__}")
    passed = 0
    for heights, expected in test_cases:
        got = solution_func(heights[:])
        if got == expected:
            passed += 1
            print(f"PASS | heights={heights} -> {got}")
        else:
            print(f"FAIL | heights={heights} -> got {got}, expected {expected}")
    print(f"Passed {passed}/{len(test_cases)} test cases.")


if __name__ == "__main__":
    run_basic_tests(largest_rectangle_area_sol1)
    # run_basic_tests(largest_rectangle_area_sol2)
    # run_basic_tests(largest_rectangle_area_sol3)
