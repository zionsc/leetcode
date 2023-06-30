class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longestSequence = 0

        for n in nums:
            if (n - 1) not in numSet: # check if it is the beginning of a sequence
                length = 0
                while (n + length) in numSet: # while sequence continues as being consecutive
                    length += 1
                longestSequence = max(length, longestSequence)
        
        return longestSequence


