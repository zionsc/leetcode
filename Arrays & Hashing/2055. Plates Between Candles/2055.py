class Solution:
    def platesBetweenCandles(self, s: str, queries: List[List[int]]) -> List[int]:
        res = []
        prefix_sum = []
        prev_candle, next_candle = [], [len(s) for _ in range(len(s))]

        curr = 0
        prev = -1
        for i in range(len(s)):
            if s[i] == '*':
                curr += 1
            else:
                prev = i
            prev_candle.append(prev)
            prefix_sum.append(curr)
        
        nxt = len(s)
        for i in range(len(s) - 1, -1, -1):
            if s[i] == '|':
                nxt = i
            next_candle[i] = nxt

        for left, right in queries:
            left = next_candle[left]
            right = prev_candle[right]
            if left != -1 and right != -1 and left < right:
                res.append(prefix_sum[right] - prefix_sum[left])
            else:
                res.append(0)

        return res