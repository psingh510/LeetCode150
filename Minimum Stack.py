class MinStack:

    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        minimum_val = min(self.minStack[-1] if self.minStack else val ,val)
        self.minStack.append(minimum_val)
        
    def pop(self) -> None:
        self.stack = self.stack[:-1]
        self.minStack = self.minStack[:-1]

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.minStack[-1]
        
