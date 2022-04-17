class CQueue:
    def __init__(self):
        self.in_stack = []
        self.out_stack = []

    def appendTail(self, value: int) -> None:
        self.in_stack.append(value)

    def deleteHead(self) -> int:
        if self.out_stack:
            return self.out_stack.pop()
        if not self.in_stack:
            return -1
        while self.in_stack:
            self.out_stack.append(self.in_stack.pop())
        return self.out_stack.pop()


# Your CQueue object will be instantiated and called as such:
# obj = CQueue()
# obj.appendTail(value)
# param_2 = obj.deleteHead()
