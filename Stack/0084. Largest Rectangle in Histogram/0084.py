class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea = 0
        stack = [] # pair (start index of rectangle, height)

        for i, h in enumerate(heights): # enumerate allows both index and value 
            start = i # start at the where it was discovered unless CHANGED BY EXTENDING BACKWARDS
            while stack and stack[-1][1] > h: # Stack is not empty, the found height is less than the stack height
                index, height = stack.pop() # pop from stack, retrieve the data from the popped bar
                maxArea = max(maxArea, height * (i - index)) # to get the area of rectangle that is popped out
                # the i - index is the width --> index is the starting index of the popped rectangle
                # the index can vary as the rectangle could have extended backwards
                start = index # update the start of the current rectangle to until the height in stack is small
            stack.append((start, h))

        for i, h in stack:
            maxArea = max(maxArea, h * (len(heights) - i)) # since the values left in the stack go from their starting index --> to the end
        
        return maxArea # return maxArea

