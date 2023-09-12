class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        # 1. make the adj. List
        # 2. use bfs --> each layer: res += 1

        if endWord not in wordList:
            return 0 
        
        wordList.append(beginWord) # must add it to wordlist in order to start from there 
        nei = defaultdict(list) # if not there, initalize it first with an empty lis
        
        for word in wordList:
            for i in word:
                pattern = word[:i] + "*" + word[i + 1:] # for each pattern, (*ot, h*t, ho*), 1 letter difference
                nei[pattern].append(word) # add that to the defaultdict

        q = collections.deque([beginWord])
        visit = set([beginWord]) # we want to see if we have already visited that word!
        res = 1

            # now BFS
        while q:
            for i in range(len(q)): # for each word in q
                word = q.popleft()
                if word == endWord:
                    return res
                for j in word:
                    pattern = word[:j] + "*" + word[j + 1:]
                    for neiWord in nei[pattern]:
                        if neiWord not in visit:
                            visit.add(neiWord)
                            q.append(neiWord)
            res += 1

        return 0 