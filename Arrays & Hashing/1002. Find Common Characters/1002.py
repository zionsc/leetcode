class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        char_array = [float('inf')] * 26
        n = len(words)
        res = []
        
        for word in words:
            word_freq = [0] * 26
            for c in word:
                word_freq[ord(c) - ord('a')] += 1
            for i in range(26):
                char_array[i] = min(char_array[i], word_freq[i])

        for i in range(26):
            if char_array[i] != float('inf') and char_array[i] != 0:
                for j in range(char_array[i]):
                    res.append(chr(i + ord('a')))

        return res
