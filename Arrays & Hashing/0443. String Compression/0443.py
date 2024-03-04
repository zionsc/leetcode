class Solution:
    def compress(self, chars: List[str]) -> int:
        l = r = 0
        res = []
        curr_count = 0
        while r < len(chars):
            if chars[l] == chars[r]:
                curr_count += 1
                r += 1
            else:
                res.append(chars[l])
                if curr_count != 1:
                    for i in range(len(str(curr_count))):
                        res.append(str(curr_count)[i])
                curr_count = 0
                l = r
        if curr_count:
            res.append(chars[l])
            if curr_count != 1:
                for i in range(len(str(curr_count))):
                    res.append(str(curr_count)[i])
        for i in range(len(res)):
            chars[i] = res[i]
        return len(res)


