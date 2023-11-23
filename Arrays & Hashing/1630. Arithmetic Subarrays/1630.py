class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        # res = []
        # for l_val, r_val in zip(l, r):
        #     temp = []
        #     val = True
        #     for i in range(l_val, r_val + 1):
        #         temp.append(nums[i])
        #     temp.sort()
        #     diff = temp[1] - temp[0]
        #     for i in range(len(temp) - 1):
        #         if temp[i + 1] - temp[i] != diff:
        #             val = False
        #             break
        #     res.append(val)
        # return res

        subarrays = []
        res = []
        for i in range(len(l)):
            subarrays.append(nums[l[i]:r[i] + 1])
        
        for subarray in subarrays:
            subarray.sort()
        
        for subarray in subarrays:
            if len(subarray) <= 2:
                res.append(True)
                continue
            diff = subarray[1] - subarray[0]
            for i in range(len(subarray) - 1):
                if subarray[i + 1] - subarray[i] != diff:
                    res.append(False)
                    break
                elif i == len(subarray) - 2:
                    res.append(True)
        return res




