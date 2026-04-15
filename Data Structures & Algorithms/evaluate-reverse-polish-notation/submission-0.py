class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        # This is simple and easy. Every time you hit one of the operands, you pop the last two stack elements
        # Perform the operation and add the result back to the stack so that we can continue the operations
        # If is not one of the operands then simply add it to the stack to be popped later on in the loop
        
        stack = []
        for c in tokens:
            if c == "+":
                stack.append(stack.pop() + stack.pop())
            elif c == "-":
                a, b = stack.pop(), stack.pop()
                stack.append(b - a)
            elif c == "*":
                stack.append(stack.pop() * stack.pop())
            elif c == "/":
                a, b = stack.pop(), stack.pop()
                stack.append(int(float(b) / a))
            else:
                stack.append(int(c))
        return stack[0]