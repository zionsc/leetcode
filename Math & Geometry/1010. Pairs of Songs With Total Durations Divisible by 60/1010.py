class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        res = 0
        freq_map = Counter(t % 60 for t in time)

        for i,v in freq_map.items():
            if 60 - i in freq_map and v > 0 and freq_map[60 - i] > 0 or i == 0:
                if i == 30 or i == 0:
                    res += comb(v, 2)
                    freq_map[i] = 0
                else:
                    res += v * freq_map[60 - i]
                    freq_map[i] = 0
                    freq_map[60 - i] = 0
        return res