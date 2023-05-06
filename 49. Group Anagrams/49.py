class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list) # mapping charCount to list of Anagrams

        for s in strs: # each string
            count = [0] * 26 # a ... z --> creating 26 0s in the array

            for c in s: # each character
                count[ord(c) - ord("a")] += 1 # incrementing that location by 1 in the array 

            res[tuple(count)].append(s)

        return res.values()