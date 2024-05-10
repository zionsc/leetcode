class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        n=len(arr)
        l,r=0,1
        res=[0,1]

        while True:
            m=(l+r)/2
            res[0]=0
            j=1
            count=0
            for i in range(n):
                j=i+1
                while j<n and arr[i]/arr[j]>m:
                    j+=1
                if j==n:
                    break
                count+=n-j
                if res[0]/res[1]<arr[i]/arr[j]:
                    res[0],res[1]=arr[i],arr[j]
            if count<k:
                l=m
            elif count>k:
                r=m
            else:
                return res
