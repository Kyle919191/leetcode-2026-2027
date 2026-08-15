"""
LeetCode 567 - Permutation in String
"""


def check_inclusion_sol1(s1: str, s2: str) -> bool:
    window = {}
    need = {}
    for element in s1:
        # TODO-TALK: I first record the required frequency of each character from s1.
        need[element] = need.get(element, 0) + 1
    
    left = right = valid = 0

    while right < len(s2):
        expanded = s2[right]
        right+=1
        
        if expanded in need:
            # TODO-TALK: On expansion, I only track characters that matter for s1.
            window[expanded] = window.get(expanded, 0) + 1
            if window[expanded] == need[expanded]:
                valid += 1
        
        while (right - left) >= len(s1): # different case compared to minimum_window_substring
            # NOTE: this check makes sure the window is never larger than len(t), because as soon as it hits len(t) size, it starts decrementing
            # realistically, we could change while (right - left) >= len(s1) to while (right - left) == len(s1) IF we check for len(s1) == 0 case
            # if we don't check this case, then after first expansion, we'll never be able to pass right - left >= len(s1) bc len(s1) is 0
            if valid == len(need): # we have all copies of what we need, permutation must exist
                # TODO-TALK: All required counts match in a window of size len(s1), so permutation exists.
                return True 
            
            shrinked = s2[left]
            left += 1
            
            if shrinked in need:
                # TODO-TALK: On shrink, if I break an exact match, I decrement valid first.
                if window[shrinked] == need[shrinked]:
                    valid -= 1
                window[shrinked] -= 1
    return False





# Solution 2


def check_inclusion_sol2(s1: str, s2: str) -> bool:
    raise NotImplementedError("Implement check_inclusion_sol2")


def check_inclusion_sol3(s1: str, s2: str) -> bool:
    raise NotImplementedError("Implement check_inclusion_sol3")


def run_basic_tests(solution_func) -> None:
    test_cases = [
        ("ab", "eidbaooo", True),
        ("ab", "eidboaoo", False),
        ("adc", "dcda", True),
    ]
    print(f"\nTesting: {solution_func.__name__}")
    passed = 0
    for s1, s2, expected in test_cases:
        got = solution_func(s1, s2)
        if got == expected:
            passed += 1
            print(f'PASS | s1="{s1}", s2="{s2}" -> {got}')
        else:
            print(f'FAIL | s1="{s1}", s2="{s2}" -> got {got}, expected {expected}')
    print(f"Passed {passed}/{len(test_cases)} test cases.")


if __name__ == "__main__":
    # run_basic_tests(check_inclusion_sol1)
    # run_basic_tests(check_inclusion_sol2)
    # run_basic_tests(check_inclusion_sol3)
    pass
