class Solution:
    def maximumLength(self, s: str) -> int:
        n = len(s)
        c = Counter()
        for i in range(1, n+1):
            for j in range(i):
                ss = s[j:i]
                if len(set([x for x in ss])) == 1:
                    c[ss] += 1
        ans = -1
        for k, v in c.items():
            if v >= 3:
                ans = max(len(k), ans)
        return ans
                