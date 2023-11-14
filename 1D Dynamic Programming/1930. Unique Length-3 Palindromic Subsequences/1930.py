class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        # res = 0
        # characters = {chr(x) for x in range(97,123,1)}
        # for k in characters:
        #     first,last = s.find(k),s.rfind(k)
        #     if first!=-1:
        #         res+=len(set(s[first+1:last]))
        # return res

# class Solution:
#     def countPalindromicSubsequence(self, s: str) -> int:
        # if not s:
        #     return 0
        
        # res = 0
        # freq = [[0] * 26 for i in range(len(s))] # i=index, j=character --> stores number of times it appears until then
        # freq[0][ord(s[0]) - 97] = 1
        # index_map = defaultdict(list)

        # for i in range(1, len(s)):
        #     for j in range(26):
        #         freq[i][j] = freq[i - 1][j] + (1 if j == ord(s[i]) - 97 else 0)

        # for i in range(len(s)):
        #     index_map[s[i]].append(i)

        # for char, index_list in index_map.items():
        #     if len(index_list) < 2:
        #         continue
        #     first, last = index_list[0], index_list[-1]
        #     for i in range(26):
        #         if freq[last - 1][i] - freq[first][i] > 0:
        #             res += 1
        # return res

        res = 0
        freq = {chr(x) for x in range(97, 123, 1)}
        for k in freq:
            first, last = s.find(k), s.rfind(k)
            if first != -1:
                res += len(set(s[first + 1:last]))

        return res



        



        

            
            
        



