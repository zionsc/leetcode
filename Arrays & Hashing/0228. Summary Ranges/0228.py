class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums:
            return []
        res = []
        start = end = nums[0]

        for i in range(1, len(nums)):
            if nums[i] == end + 1:
                end = nums[i]
            else:
                if start == end:
                    res.append(f"{start}")
                else:
                    res.append(f"{start}->{end}")
                start = end = nums[i] # doesn't do the last part here for the last index!!

        if start == end:
            res.append(f"{start}")
        else:
            res.append(f"{start}->{end}")
        return res
        


        