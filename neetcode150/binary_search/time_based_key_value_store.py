"""
LeetCode 981 - Time Based Key-Value Store
"""


class TimeMapSol1:
    def __init__(self):
        self.store = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store:
            self.store[key] = []
        self.store[key].append((timestamp, value))
        # equivalent to self.store.setdefault(key, []).append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.store:
            return ""
        arr = self.store[key]
        left = 0
        right = len(arr) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if arr[mid][0] <= timestamp:
                # TODO-TALK: This value is valid candidate; search right for newer valid one.
                answer = arr[mid][1]
                left = mid + 1
            else:
                right = mid - 1
        return answer
        


def run_basic_tests(time_map_class) -> None:
    print(f"\nTesting: {time_map_class.__name__}")
    tm = time_map_class()
    tm.set("foo", "bar", 1)
    r1 = tm.get("foo", 1)
    r2 = tm.get("foo", 3)
    tm.set("foo", "bar2", 4)
    r3 = tm.get("foo", 4)
    r4 = tm.get("foo", 5)
    got = [r1, r2, r3, r4]
    expected = ["bar", "bar", "bar2", "bar2"]
    if got == expected:
        print(f"PASS | got={got}")
    else:
        print(f"FAIL | got={got}, expected={expected}")


if __name__ == "__main__":
    run_basic_tests(TimeMapSol1)

