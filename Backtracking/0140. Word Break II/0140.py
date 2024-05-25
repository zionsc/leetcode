class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        res=[]
        wordSet=set(wordDict)
        n=len(s)

        def sentenceBacktrack(sentence:List[str], start_idx:int) -> None:
            if (start_idx==n):
                res.append(" ".join(sentence))
                return
        
            for end_idx in range(start_idx, n):
                word=s[start_idx : end_idx+1]
                if (word in wordSet):
                    sentence.append(word)
                    sentenceBacktrack(sentence, end_idx+1)
                    sentence.pop()

        sentenceBacktrack([],0)
        return res