class BinaryMinHeap:
    def __init__(self):
        self.heap: list[int] = []

    # ---------- index helpers ----------
    def _parent(self, i: int) -> int:
        return (i - 1) // 2

    def _left(self, i: int) -> int:
        return 2 * i + 1

    def _right(self, i: int) -> int:
        return 2 * i + 2

    # ---------- core operations ----------
    def peek(self) -> int | None:
        if not self.heap:
            return None
        return self.heap[0]

    def push(self, value: int) -> None:
        self.heap.append(value)
        self._sift_up(len(self.heap) - 1)

    def pop(self) -> int | None:
        if not self.heap:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()

        min_value = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._sift_down(0)
        return min_value

    def __len__(self) -> int:
        return len(self.heap)

    # ---------- internal maintenance ----------
    def _sift_up(self, i: int) -> None:
        while i > 0:
            p = self._parent(i)
            if self.heap[p] <= self.heap[i]:
                break
            self.heap[p], self.heap[i] = self.heap[i], self.heap[p]
            i = p

    def _sift_down(self, i: int) -> None:
        n = len(self.heap)
        while True:
            left = self._left(i)
            right = self._right(i)
            smallest = i

            if left < n and self.heap[left] < self.heap[smallest]:
                smallest = left
            if right < n and self.heap[right] < self.heap[smallest]:
                smallest = right

            if smallest == i:
                break
            self.heap[i], self.heap[smallest] = self.heap[smallest], self.heap[i]
            i = smallest


# -------------------------------
# 1) Class-based binary min heap
# -------------------------------
min_heap = BinaryMinHeap()
min_heap.push(5)
min_heap.push(2)
min_heap.push(8)
min_heap.push(1)

# Current heap array (one possible valid min-heap):
# [1, 2, 8, 5]

# Example operations:
# min_heap.peek() -> 1
# min_heap.pop()  -> 1
# min_heap.peek() -> 2


# ------------------------------------
# 2) Array view of the same structure
# ------------------------------------
# For array index i:
# parent = (i - 1) // 2
# left   = 2 * i + 1
# right  = 2 * i + 2
#
# Example:
# i = 0 (value 1) -> children at 1 and 2 (values 2 and 8)
# i = 1 (value 2) -> children at 3 and 4 (value 5 and out-of-range)
