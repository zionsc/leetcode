class Solution:
    def calculateTime(self, keyboard: str, word: str) -> int:
        res = 0
        position = 0
        locations = defaultdict(int)
        for i in range(len(keyboard)):
            locations[keyboard[i]] = i

        for c in word:
            res += abs(position - locations[c])
            position = locations[c]

        return res
