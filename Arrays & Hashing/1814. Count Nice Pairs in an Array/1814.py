class Solution:
    def countNicePairs(self, nums: List[int]) -> int:
        MOD = (10**9) + 7
        freq_map = defaultdict(int)
        cnt = 0
        
        for i in range(len(nums)):
            nums[i] = nums[i] - int(str(nums[i])[::-1])
            freq_map[nums[i]] += 1
        
        for i,v in freq_map.items():
            cnt += comb(v, 2)
            cnt %= MOD
        return cnt % MOD

# class Solution:
#     def countNicePairs(self, nums: List[int]) -> int:
#         nums = [i - int(str(i)[::-1]) for i in nums]
#         res = 0
#         for n in Counter(nums).values():
#             res += n*(n-1)//2 
#         return res % (10**9 + 7)

# class Solution:
#     def countNicePairs(self, nums: List[int]) -> int:
#         mod=10**9+7
#         ans=0
#         count=collections.Counter()
#         for num in nums:
#             num-=int(str(num)[::-1])
#             ans+=count[num]
#             count[num]+=1
#         return ans%mod     