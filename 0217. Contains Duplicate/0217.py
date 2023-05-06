class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashset = set() # there is no such thing as a hashset in python --> only set 

        for i in nums:
            if i in hashset:
                return True
            hashset.add(i)

        return False