class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        num = 0
        op = '+'

        # the + at the end to parse the last operation --> basically this funct does the last operation found
        for c in s + '+':
            if c.isdigit():
                num = (num * 10) + int(c)
            elif c == ' ':
                continue
            else: # c is an operation
                if op == '+':
                    stack.append(num)
                elif op == '-':
                    stack.append(-num)
                elif op == '*':
                    stack.append(stack.pop() * num)
                elif op == '/':
                    stack.append(int(stack.pop() / num))

                num = 0
                op = c

        return sum(stack)