class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        freq = Counter(arr)
        unique = set()
        for i,v in freq.items():
            if v in unique:
                return False
            unique.add(v)
        return True