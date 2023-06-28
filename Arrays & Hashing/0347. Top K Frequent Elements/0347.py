class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = [[] for i in range(len(nums) + 1)]

        for n in nums: # adding to count hashmap
            count[n] = 1 + count.get(n, 0)
        for n, c in count.items(): # key value pair n, c
            freq[c].append(n) # index is number of times it exists, n is the actual number in nums

        res = []
        for i in range(len(freq)-1, 0, -1):
            for j in freq[i]:
                res.append(j)
                k -= 1
                if k == 0:
                    return res
