class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        my_map = defaultdict(int)

        for i, n in enumerate(nums):
            # basically if num has been seen before, then the next time we see it if the current map[n] is the closest
            # last time we saw n, thus my_map[n] - i would be the smallest. we need it to be smaller then k so yes!!!
            if n in my_map and abs(my_map[n] - i) <= k:
                return True
            else: # otherwise swap the my_map[n] to the current index of n --> i
                my_map[n] = i
        
        return False
