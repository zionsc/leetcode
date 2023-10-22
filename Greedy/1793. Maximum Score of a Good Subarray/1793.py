class Solution:
    def maximumScore(self, nums: List[int], k: int) -> int:

        res = mini = nums[k] * (k - k + 1)
        i, j = k, k

        # because i,j incremented last time in the loop itself (must do or since one may be already at 0 or len(nums))
        while i > 0 or j < len(nums) - 1:
            if i == 0:
                j += 1
            elif j == len(nums) - 1:
                i -= 1
            elif nums[i - 1] < nums[j + 1]:
                j += 1
            else:
                i -= 1
            
            # no need to check every value in between as it iterates from 0<--k-->len(nums), so it will update for min each time
            mini = min(mini, nums[i], nums[j]) 
            res = max(res, mini * (j - i + 1))
        
        return res

