class Solution:
    def isValid(self, s: str) -> bool:
        CloseToOpen = {")": "(", "]": "[", "}": "{"}
        stack = []
 
        for c in s:
            if c in CloseToOpen: # checking the key, thus checking if c is a closing parenthesis
                if stack and stack[-1] == CloseToOpen[c]: # if stack is not empty && last open parenthesis matches closing parenthesis
                    stack.pop()
                else:
                    return False
            else: # NOT a closing paranthesis
                stack.append(c)

        return True if not stack else False # only return true if stack is empty else return False
