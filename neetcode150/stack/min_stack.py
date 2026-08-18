"""
LeetCode 155 - Min Stack
"""


class MinStackSol1:
    def __init__(self):
        self.stack = []
        self.minstack = []
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.minstack:
            self.minstack.append(val)
        else:
            # TODO-TALK: Track current minimum at every push.
            # remembers the minimum at every historical stack size
            self.minstack.append(min(val, self.minstack[-1]))

    def pop(self) -> None:
        self.stack.pop()
        self.minstack.pop()

    def top(self) -> int:
       return self.stack[-1]

    def getMin(self) -> int:
        return self.minstack[-1]



def run_basic_tests(stack_class) -> None:
    print(f"\nTesting: {stack_class.__name__}")
    stk = stack_class()
    stk.push(-2)
    stk.push(0)
    stk.push(-3)
    r1 = stk.getMin()
    stk.pop()
    r2 = stk.top()
    r3 = stk.getMin()
    got = [r1, r2, r3]
    expected = [-3, 0, -2]
    if got == expected:
        print(f"PASS | got={got}")
    else:
        print(f"FAIL | got={got}, expected={expected}")


if __name__ == "__main__":
    run_basic_tests(MinStackSol1)

