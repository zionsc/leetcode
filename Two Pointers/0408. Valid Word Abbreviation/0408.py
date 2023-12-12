class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        w = a = 0
        # TODO // check for case that abbr IS JUST numbers

        while w < len(word) and a < len(abbr):
            if abbr[a].isalpha() and abbr[a] == word[w]:
                w += 1
                a += 1
                continue
            elif abbr[a] == '0':
                return False
            elif abbr[a].isnumeric():
                cnt = 0
                while a < len(abbr) and abbr[a].isnumeric():
                    cnt = cnt * 10 + int(abbr[a])
                    a += 1
                w += cnt
            else:
                return False

        return w == len(word) and a == len(abbr)
                
