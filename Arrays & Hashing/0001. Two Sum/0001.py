class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        mylist = []

        for i in range(len(nums)):
            hashmap[nums[i]] = i
        
        for i in range(len(nums)):
            if (target - nums[i]) in hashmap and i != hashmap[target-nums[i]]:
                mylist.append(i)
                mylist.append(hashmap[target-nums[i]])
                return mylist

        return mylist