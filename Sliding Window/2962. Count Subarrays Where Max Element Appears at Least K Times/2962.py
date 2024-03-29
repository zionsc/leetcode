class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        number=max(nums)
        l=res=curr=0

        for r in range(len(nums)):
            if nums[r]==number:
                curr+=1
            while curr==k:
                if nums[l]==number:
                    curr-=1
                l+=1
            res+=l
        return res
