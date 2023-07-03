class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = [] # pair (temp, index)

        for i, t in enumerate(temperatures): # enumerate must be used in order to get both index and value
            # this works as the values that are skipped over will be checked by stack as they are popped
            while stack and t > stack[-1][0]:
                temp, index = stack.pop()
                res[index] = i - index
            stack.append((t, i)) # if the current temp is less than the last temp, add it to the stack

        return res
    