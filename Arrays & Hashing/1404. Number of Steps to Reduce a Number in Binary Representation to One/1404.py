class Solution:
    def numSteps(self, s: str) -> int:
        s=list(s)
        res=0
        while (len(s)>1):
            if (s[-1]=='0'): s.pop()
            else:
                i=len(s)-1
                while (i>=0 and s[i]=='1'):
                    s[i]='0'
                    i-=1
                if (i>=0): s[i]='1'
                else: s.insert(0,'1')
            res+=1
        return res