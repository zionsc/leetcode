class Solution:
    def customSortString(self, order: str, s: str) -> str:
        count = Counter(s)
        ans = []

        for c in order:
            ans.append(c * count[c])
            count[c] = 0
        
        for c in s:
            ans.append(c * count[c])

        return "".join(ans)

