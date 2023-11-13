class Solution:
    def sortVowels(self, s: str) -> str:
        my_map = {'A': 0, 'E': 0, 'I': 0, 'O': 0, 'U': 0, 'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}
        s_list = []
        
        for i in s:
            s_list.append(i)
            if i in my_map:
                my_map[i] += 1
        
        for i in range(len(s)):
            if s[i] in my_map:
                for j, v in my_map.items():
                    if v > 0:
                        s_list[i] = j
                        my_map[j] -= 1
                        break

        return "".join(s_list)

