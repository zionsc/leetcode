class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2):
            return False

        for c1,c2 in zip(word1, word2):
            if c1 not in word2 or c2 not in word1:
                return False

        word1_lst = list(Counter(word1).values())
        word2_lst = list(Counter(word2).values())

        if sorted(word1_lst) == sorted(word2_lst):
            print(sorted(word1_lst), sorted(word2_lst))
            return True
        return False