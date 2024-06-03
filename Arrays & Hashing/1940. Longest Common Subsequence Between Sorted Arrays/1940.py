class Solution:
    def longestCommonSubsequence(self, arrays: List[List[int]]) -> List[int]:
        res = arrays[0].copy()
        for i in range(1, len(arrays)):
            res = self.find_LCS(res, arrays[i])
        return res

        
    def find_LCS(self, arr1: List[int], arr2: List[int]) -> List[int]:
        arr1_counter = Counter(arr1)
        arr2_counter = Counter(arr2)

        ret = []

        for num, count in arr1_counter.items():
            if arr2_counter[num] == count:
                ret.append(num)
    
        return ret

        