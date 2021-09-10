class MyQueue:
    
    def __init__(self):
        # do intialization if necessary
        self.stack = []
    """
    @param: element: An integer
    @return: nothing
    """
    def push(self, element):
        return self.stack.append(element)        

    """
    @return: An integer
    """
    def pop(self):
        return self.stack.pop(0)
    """
    @return: An integer
    """
    def top(self):
        return self.stack[0]
