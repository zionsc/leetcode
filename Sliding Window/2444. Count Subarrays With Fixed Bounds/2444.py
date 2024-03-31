class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        lastMax=lastMin=-1
        l=res=0

        for r in range(len(nums)):
            if nums[r]<minK or nums[r]>maxK:
                l=r+1
                lastMax=lastMin=-1
            if nums[r]==minK:
                lastMin=r
            if nums[r]==maxK:
                lastMax=r
            if lastMin!=-1 and lastMax!=-1:
                res+=min(lastMin,lastMax)-l+1
        return res