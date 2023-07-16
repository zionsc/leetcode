class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        output = []

        # creating a queue in python
        q = collections.deque()

        # left and right pointers in order to 
        l = r = 0

        while r < len(nums):
            