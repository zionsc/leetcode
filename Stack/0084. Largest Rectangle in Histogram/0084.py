class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea = 0
        stack = [] # pair (start index of rectangle, height)

        for i, h in enumerate(heights): # enumerate allows both index and value 
            start = i # start at the where it was discovered unless CHANGED BY EXTENDING BACKWARDS

            # Basically the idea of the while loop is to pop all values of the stack that are greater in height than the discovered bar. -->
            # before popping though, the maxArea for them would be compared to the current maxArea (maxArea for them could extend backwards, thats why we update start accordingly)
            # do this until the bar's height no longer is less than the stack[-1], meaning that the rectangle created by this bar starts at that given index. 
            # Always make the index of the bar in the stack be the start value fo the rectangle given that the rectangle extends backwards as far as it can
            # values that are simply just added as they are the tallest bar would have their start index just be where they were discovered as they cannot extend backwards. 

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

