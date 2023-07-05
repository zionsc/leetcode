class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # 1-indexed array

        l, r = 0, len(numbers) - 1


        # Basically using the fact that it is sorted to our advantage. 
        # It will always either be greater or smaller or the sum.
        
        while l < r:
            if (numbers[l] + numbers[r] == target):
                return [l + 1, r + 1]
            elif (numbers[l] + numbers[r] > target):
                r -= 1
            elif (numbers[l] + numbers[r] < target):
                l += 1

        return [l + 1, r + 1] 



