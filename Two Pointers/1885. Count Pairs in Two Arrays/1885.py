class Solution:
    def countPairs(self, nums1: List[int], nums2: List[int]) -> int:
        nums3=[a-b for a,b in zip(nums1,num2)]
        nums3.sort()
        
        res=0
        l,r=0,len(nums3)-1
        while(l<r):
            if(nums3[l]+nums3[r]>0):
                res+=r-l
            else:
                r-=1
                l+=1
        return res