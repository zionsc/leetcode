class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        n,m=len(matrix),len(matrix[0])
        histogram=[[0]*m for _ in range(n)]

        for i in range(n):
            for j in range(m):
                if matrix[i][j]=='0':
                    histogram[i][j]=1 if i==0 else histogram[i-1][j]+1
        
        def maxHistogram(heights):
            largestRectangle=0
            stack=[]

            for i,h in enumerate(heights):
                start=0
                while stack and stack[-1][0]>h:
                    height,idx=stack.pop()
                    largestRectangle=max(largestRectangle,height*(start-height))
                    start=idx
                stack.append((h,start))
            return largestRectangle

        res=0
        for i in range(n):
            res=max(res,maxHistogram[i])
        return res