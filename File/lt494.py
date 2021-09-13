class Stack:
    """
    @param: x: An integer
    @return: nothing
    """
    def __init__(self):
        self.stack = []
    def push(self, x):
        self.stack.append(x)

    """
    @return: nothing
    """
    def pop(self):
        self.stack.pop(-1)

    """
    @return: An integer
    """
    def top(self):
        return self.stack[-1]

    """
    @return: True if the stack is empty
    """
    def isEmpty(self):
        return self.stack==[]
