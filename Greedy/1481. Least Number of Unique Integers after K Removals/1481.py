class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        freq_map = Counter(arr)
        sorted_values = sorted(freq_map.values())
        res = len(freq_map.keys())

        for value in sorted_values:
            if k >= value:
                k -= value
                res -= 1
            else:
                break

        return res