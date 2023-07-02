class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        my_stack = []
        
        for n in tokens:
            if n == "+":
                a, b = my_stack.pop(), my_stack.pop()
                my_stack.append(a + b)
            elif n == "-":
                a, b = my_stack.pop(), my_stack.pop()
                my_stack.append(b - a) 
            elif n == "*":
                a, b = my_stack.pop(), my_stack.pop()
                my_stack.append(a * b)
            elif n == "/":
                a, b = my_stack.pop(), my_stack.pop()
                my_stack.append(int(b / a)) # must truncate (round) value to 0 --> division is not integer division!
            else:
                my_stack.append(int(n))

        return my_stack[0]
