class Solution:
    def makeGood(self, s: str) -> str:
        stack=[]
        for i in range(len(s)):
            if stack and stack[-1].upper()==s[i].upper() and ord(stack[-1])-ord(s[i])!=0:
                stack.pop()
            else:
                stack.append(s[i])
        return "".join(stack)