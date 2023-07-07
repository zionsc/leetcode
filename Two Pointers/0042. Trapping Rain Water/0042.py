class Solution:
    def trap(self, height: List[int]) -> int:
        # if height array is empty
        if not height: return 0

        l, r = 0, len(height) - 1
        maxLeft, maxRight = height[l], height[r]

        # res can be initialized to 0 because we know no water can be held at the endpoints
        res = 0

        while l < r:
            # maxLeft is the bottleneck
            if maxLeft < maxRight:
                l += 1
                # new bottleneck is the bigger one between old bottleneck and new left pointer
                maxLeft = max(maxLeft, height[l])
                # If no water can be held, it will simply be 0 (height[l] - height[l]). 
                # Else, height[l] is lower than the bottleneck, thus it can hold some water!
                    # Max water it can hold is the gap between itself as the bottleneck (we know leftmax is smaller than rightmax)
                    # ^^ Thus, we don't need to know the right side height as the leftmost and rightmost tallest bars will hold water up to there anyways
                res += maxLeft - height[l]
            # maxRight is the bottleneck
            else:
                r -= 1
                maxRight = max(maxRight, height[r])
                res += maxRight - height[r]
            
            return res