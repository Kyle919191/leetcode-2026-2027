"""
LeetCode 49 - Group Anagrams
"""


def group_anagrams_sol1(strs: list[str]) -> list[list[str]]:
    result = {}

    for elem in strs:
        freq = [0] * 26
        for s in elem:
            freq[ord(s) - ord('a')] += 1
        freq_tuple = tuple(freq) # use the frequency of characters as key
        # this way, two anagrams will fall in the same key as their freq is the same
        if freq_tuple not in result:
            result[freq_tuple] = []
        result[freq_tuple].append(elem)
    return list(result.values())



def group_anagrams_sol2(strs: list[str]) -> list[list[str]]:
    raise NotImplementedError("Implement group_anagrams_sol2")


def group_anagrams_sol3(strs: list[str]) -> list[list[str]]:
    raise NotImplementedError("Implement group_anagrams_sol3")


def normalize(groups: list[list[str]]) -> list[list[str]]:
    return sorted([sorted(g) for g in groups])


def run_basic_tests(solution_func) -> None:
    test_cases = [
        (["eat", "tea", "tan", "ate", "nat", "bat"], [["bat"], ["nat", "tan"], ["ate", "eat", "tea"]]),
        ([""], [[""]]),
        (["a"], [["a"]]),
    ]
    print(f"\nTesting: {solution_func.__name__}")
    passed = 0
    for strs, expected in test_cases:
        got = solution_func(strs[:])
        if normalize(got) == normalize(expected):
            passed += 1
            print(f"PASS | strs={strs} -> {got}")
        else:
            print(f"FAIL | strs={strs} -> got {got}, expected {expected}")
    print(f"Passed {passed}/{len(test_cases)} test cases.")


if __name__ == "__main__":
    run_basic_tests(group_anagrams_sol1)
    # run_basic_tests(group_anagrams_sol2)
    # run_basic_tests(group_anagrams_sol3)

