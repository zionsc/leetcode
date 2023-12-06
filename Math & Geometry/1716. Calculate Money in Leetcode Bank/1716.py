class Solution:
    def totalMoney(self, n: int) -> int:
        res = 0
        weeks = n // 7
        days_last_week = n % 7
        week = 0

        for i in range(1, weeks + 1):
            res += (7 * (7 + 1)) // 2
            res += 7 * weeks
            weeks += 1
        
        res += (days_last_week * (days_last_week + 1)) // 2
        res += week * days_last_week
        return res