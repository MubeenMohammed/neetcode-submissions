class MinStack:

    def __init__(self):
        self.stack = []
        # To implement the getMin() in constant time we use two stacks. One stack to store the data and 
        # Another stack to track the minimum value each point
        self.minStack = []


    def push(self, val: int) -> None:
        # First you push the value to our normal stack to track the data
        self.stack.append(val)
        # Now you calculate if the new value is smaller than the previous minimum by looking into the top value of minStack
        # prevMin = self.minStack[-1]
        # There is also an edge case where the minStack is empty and we are trying to pop the top element which does exists. To avoid this problem, we do
        prevMin = self.minStack[-1] if self.minStack else val
        # Compare and check if the new value is the new min at that point
        newMin = min(prevMin, val)
        self.minStack.append(newMin)

    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minStack[-1]
        
