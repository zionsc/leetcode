class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        n = floor(len(arr) / 4)
        for i in range(len(arr)):
            if i + n < len(arr) and arr[i] == arr[i + n]:
                return arr[i]
        return arr[0]
    


