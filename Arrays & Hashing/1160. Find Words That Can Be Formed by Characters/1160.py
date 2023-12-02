class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        res = 0
        for word in words:
            for chr in word:
                if word.count(chr) > chars.count(chr):
                    break
            else: # only executes when for loop is executed normally 
                res += len(word)
        return res




                