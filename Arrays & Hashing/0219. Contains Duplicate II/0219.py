class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        my_map = defaultdict(int)

        for i, n in enumerate(nums):
            if n in my_map and abs(my_map[n] - i) <= k:
                return True
            else:
                my_map[n] = i
        
        return False
