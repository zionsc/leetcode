class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # Basic Idea: Go through from 1 to max number in piles to see which value is the highest possible k we can have.
        # Max piles should be the biggest k as anything bigger does not really make a difference in our time. 
        l, r = 1, max(piles)
        res = max(piles)

        while l <= r:
            hours = 0
            # mid value
            k = l + ((r - l) // 2)

            for p in piles:
                

        