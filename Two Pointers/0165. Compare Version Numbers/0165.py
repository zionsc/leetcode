class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        n,m=len(version1),len(version2)
        i=j=0
        while(i<n or j<m):
            num1=num2=0
            while(i<n and version1[i]!='.'):
                num1=num1*10+(ord(version1[i])-ord('0'))
                i+=1
            i+=1
            while(j<m and version2[j]!='.'):
                num2=num2*10+(ord(version2[j])-ord('0'))
                j+=1
            j+=1
            if(num1<num2):return -1
            if(num1>num2):return 1
        
        while(i<n):
            num1=0
            while(i<n and version1[i]!='.'):
                num1=num1*10+(ord(version1[i])-ord('0'))
                i+=1
            if(num1):return 1
        while(j<m):
            num2=0
            while(j<m and version2[j]!=','):
                num2=num2*10+(ord(version2[j])-ord('0'))
                j+=1
            if(num2):return -1
        return 0 