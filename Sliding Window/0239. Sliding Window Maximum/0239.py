class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        output = []

        # creating a queue in python
        q = collections.deque() # contains the index of the value instead in order to check for out of bounds in sliding window, simply do nums[i] for value

        # left and right pointers in order to 
        l = r = 0

        while r < len(nums):
            # we can pop the numbers from the back of the queue that are less than the current value that we are adding from the sliding window
            # we can do this because the value is the maximum, and it is the most recent one. Meaning that anything that was added before that is less than itself
            # does not need to be considered
            while q and nums[r] > nums[q[-1]]:
                q.pop()
            q.append(r)
