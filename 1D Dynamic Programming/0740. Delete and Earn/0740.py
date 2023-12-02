class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        counter = defaultdict(int)
        max_num = 0

        # the whole concept of this problem -->
        # is that the dp array contains total sum we can get considering up to the current 'num'
        # but the num that we consider is not actually the index of number in nums, but it is the num itself.
        # this is because this is essentially the house robbing problem, but we don't necessarily take
        # either left or right, but it is a group of numbers we must consider. --> thus when considering one
        # we must take out the entire thing. 
        for num in nums:
            counter[num] += num
            max_num = max(max_num, num) # gets us the maximum number

        # this means that the dp array size must go up until max_num because we are saying that 
        # if we take the max_num what is the current total possible max sum? 
        dp = [0 for _ in range(max_num + 1)]
        # thus dp[1] represents WHAT IF WE TAKE ALL THE 1s from NUMS??? --> then we get the sum of the 1s.
        # and then we basically house robber it.
        dp[1] = counter[1]

        # we start from 2 because we know 0 and 1 have been initialized already.
        for num in range(2, len(dp)):
            # this recurrence relation because we can either take the previous one or the num - 2!!! 
            # because we got to remove all num - 1 and num + 1 (num + 1 will be taken care of in future steps)
            dp[num] = max(dp[num - 1], dp[num - 2] + counter[num])

        return dp[-1] # or return dp[max_num] which is basically the same thing, because dp's indices represent
    # actual numbers in nums, not the indices of nums.
