class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        maxArea = 0

        while l < r:
            maxArea = max(maxArea, min(height[l], height[r]) * (r - l))
            
            if height[l] < height[r]:
                l += 1
            elif height[l] >= height[r]:
                r -= 1

        return maxArea