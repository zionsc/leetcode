class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []

        for i,temp in enumerate(temperatures):
            while stack and temp > stack[-1][0]:
                stack_index, stack_temp = stack.pop()
                res[stack_index] = i - stack_index
            stack.append((temp, i))

        return res