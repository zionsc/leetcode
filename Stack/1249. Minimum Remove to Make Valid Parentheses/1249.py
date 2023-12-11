class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        s_list = list(s)

        for i in range(len(s_list)):
            if s_list[i] == '(':
                stack.append(i)
            elif s_list[i] == ')':
                if stack:
                    stack.pop()
                else:
                    s_list[i] = ''
        
        while stack:
            s_list[stack.pop()] = ''

        return ''.join(s_list)