class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # only add open parenthesis if open < n
        # only add a closing paranthesis if closed < open
        # valid IFF open == closed == n

        stack = []
        res = []

        def backtrack(openN, closedN):
            if openN == closedN == n:
                res.append("".join(stack)) # join stack into a empty string, then append to res
                return

            if openN < n:
                stack.append("(")
                backtrack(openN + 1, closedN)
                stack.pop() # stack is basically a global variable, once the one combination finishes, must pop the string that we've added
                # basically recursively removes this step, backtracks.

            if closedN < openN:
                stack.append(")")
                backtrack(openN, closedN + 1)
                stack.pop()

        backtrack(0, 0)
        return res
            



