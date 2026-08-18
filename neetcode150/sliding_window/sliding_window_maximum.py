"""
LeetCode 239 - Sliding Window Maximum
"""
from collections import deque

# naive approach(going through all windows, calculate max of each) is O(nk). this is O(n)
def max_sliding_window_sol1(nums: list[int], k: int) -> list[int]:
    q= deque() # our queue stores indexes. reason why we need queue is efficient popleft(O1)
    # our queue's stored indexes will be monotonically increasing, but the values at those indexes in nums
    # are monotonically decreasing. If not, remove those useless indices
    # so at every moment, our queue has maximum k elements, often times less
    result = []

    # NOTE: we won't have a problem of accidentally procesing windows < k towards the end of the list
    # because when we process the index, we're really analyzing the window starting at i-k+1, not the window starting at i
    for i, x in enumerate(nums):
        # 1st: make sure we're only evaluating the k number of values
        # TODO-TALK: Remove indices that are outside the current window.
        while q and q[0] <= i-k: #if we're on idx 5 with k=3, valid window idx are 3, 4, 5
            q.popleft()
        # 2nd: remove elements if smaller than our current, so q[0] stores the index that has max in nums for that window
        # TODO-TALK: Keep deque decreasing so front is always max index.
        while q and x > q[-1]:
            q.pop() 
        # 3rd: now append our current index
        q.append(i)
        # 4th: when we start to have a k-sized window, start appending(onetime thing)
        if i >= k-1: 
            # TODO-TALK: Window is formed, take value at deque front as max.
            result.append(nums[q[0]])
    return result



def max_sliding_window_sol2(nums: list[int], k: int) -> list[int]:
    raise NotImplementedError("Implement max_sliding_window_sol2")


def max_sliding_window_sol3(nums: list[int], k: int) -> list[int]:
    raise NotImplementedError("Implement max_sliding_window_sol3")


def run_basic_tests(solution_func) -> None:
    test_cases = [
        ([1, 3, -1, -3, 5, 3, 6, 7], 3, [3, 3, 5, 5, 6, 7]),
        ([1], 1, [1]),
        ([9, 11], 2, [11]),
    ]
    print(f"\nTesting: {solution_func.__name__}")
    passed = 0
    for nums, k, expected in test_cases:
        got = solution_func(nums[:], k)
        if got == expected:
            passed += 1
            print(f"PASS | nums={nums}, k={k} -> {got}")
        else:
            print(f"FAIL | nums={nums}, k={k} -> got {got}, expected {expected}")
    print(f"Passed {passed}/{len(test_cases)} test cases.")


if __name__ == "__main__":
    run_basic_tests(max_sliding_window_sol1)
    # run_basic_tests(max_sliding_window_sol2)
    # run_basic_tests(max_sliding_window_sol3)
    pass
