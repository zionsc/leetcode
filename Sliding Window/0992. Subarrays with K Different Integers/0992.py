class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        def atMostK(arr,K):
            freq = defaultdict(int)
            l=res=0
            for r in range(len(arr)):
                freq[arr[r]]+=1
                if freq[arr[r]]==1:
                    K-=1
                while K<0:
                    freq[arr[l]]-=1
                    if freq[arr[l]]==0:
                        K+=1
                    l+=1
                res+=(r-l+1)
            return res  

        return atMostK(nums,k) - atMostK(nums,k-1)