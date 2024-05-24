class Solution:
    def word_backtrack(self, w_idx:int, currMax:int) -> None:
        if (w_idx==self.n):
            self.res=max(self.res, currMax)
            return
        check=True
        count=Counter(self.word_list[w_idx])
        for i,v in count.items():
            if (v>self.freq[i]):
                check=False
        if (check and self.letter_backtrack(self.word_list[w_idx], 0)):
            temp=0
            for c in self.word_list[w_idx]:
                temp+=self.value[ord(c)-ord('a')]
            for c in self.word_list[w_idx]:
                self.freq[c]-=1
            self.word_backtrack(w_idx+1, temp+currMax)
            for c in self.word_list[w_idx]:
                self.freq[c]+=1
        self.word_backtrack(w_idx+1, currMax)


    def letter_backtrack(self, word:str, idx:int) -> bool:
        if (idx==len(word)):
            return True
        if (self.freq[word[idx]]==0):
            return False
        return self.letter_backtrack(word, idx+1)
        

    def maxScoreWords(self, words: List[str], letters: List[str], score: List[int]) -> int:
        self.n=len(words)
        self.freq=Counter(letters)
        self.value=score
        self.word_list=words
        self.res=0
        self.word_backtrack(0,0)
        return self.res
