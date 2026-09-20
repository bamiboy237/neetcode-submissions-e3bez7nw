class MinStack:

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        curr_min = min(val, self.getMin()) if self.stack else val
        self.stack.append((val, curr_min))

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.stack[-1][1]
        
