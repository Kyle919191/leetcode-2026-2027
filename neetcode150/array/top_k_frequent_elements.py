"""
LeetCode 347 - Top K Frequent Elements
"""


def top_k_frequent_sol1(nums: list[int], k: int) -> list[int]:
    freq = {}
    for num in nums:
        freq[num] = freq.get(num, 0) + 1
    
    # we can just sort the freq dictionary by the values, but it would be O(m log m) time, where m = unique numbers
    bucket = [[] for _ in range(len(nums) + 1)] # [[] * (len(nums)+ 1)] is wrong
    for elem, frequency in freq.items():
        bucket[frequency].append(elem) # use list with index-element as dictionary key-pair is a common approach
        # for example, all the ord('A') cases

    result = []

    for f in range(len(bucket) - 1, 0, -1):
        for element in bucket[f]: # in the bucket, each element is a list because there might be more than one element for each frequency
            result.append(element)
            if len(result) == k:
                return result
    # all done in linear time
    return result


import heapq
def top_k_frequent_sol2(nums: list[int], k: int) -> list[int]:
    freq = {}
    for num in nums:
        freq[num] = freq.get(num, 0) + 1
    
    # we use min heap, pop until heap has k elements
    heap: list[tuple[int, int]] = []
    for elem, frequency in freq.items():
        heapq.heappush(heap, (frequency, elem)) # frequency has to come before elem, as we use that as sort
    while len(heap) > k:
        heapq.heappop(heap)
    return [number for _, number in heap]



def top_k_frequent_sol3(nums: list[int], k: int) -> list[int]:
    raise NotImplementedError("Implement top_k_frequent_sol3")


def run_basic_tests(solution_func) -> None:
    test_cases = [
        ([1, 1, 1, 2, 2, 3], 2, [1, 2]),
        ([1], 1, [1]),
        ([4, 1, -1, 2, -1, 2, 3], 2, [-1, 2]),
    ]
    print(f"\nTesting: {solution_func.__name__}")
    passed = 0
    for nums, k, expected in test_cases:
        got = solution_func(nums[:], k)
        if sorted(got) == sorted(expected):
            passed += 1
            print(f"PASS | nums={nums}, k={k} -> {got}")
        else:
            print(f"FAIL | nums={nums}, k={k} -> got {got}, expected {expected}")
    print(f"Passed {passed}/{len(test_cases)} test cases.")


if __name__ == "__main__":
    run_basic_tests(top_k_frequent_sol1)
    run_basic_tests(top_k_frequent_sol2)
    # run_basic_tests(top_k_frequent_sol3)

