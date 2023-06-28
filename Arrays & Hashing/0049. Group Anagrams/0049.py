class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list) # mapping charCount to list of Anagrams

        for s in strs: # each string
            count = [0] * 26 # a ... z --> creating 26 0s in the array, basically an ID for each anagram
            for c in s: # each character
                count[ord(c) - ord("a")] += 1 # incrementing that location by 1 in the array, ord() returns unicode 
            res[tuple(count)].append(s) # group all anagrams that have that count to one list --> lists cannot be keys (they can be changed, thus tuple.)
            # basically each anagram has a ID (count) and we group all anagrams that have the same ID to one list
        return res.values()
    
    # count --> [0, 0, 0, 0, 0, 0...n] ID for each anagram --> group all anagrams that have the same ID to one list
