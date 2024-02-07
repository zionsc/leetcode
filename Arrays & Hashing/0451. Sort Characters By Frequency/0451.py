class Solution:
    def frequencySort(self, s: str) -> str:
        freq = Counter(s)
        keys = sorted(freq.keys(), key=lambda x:(-freq[x], x))
        return "".join(key * freq[key] for key in keys)