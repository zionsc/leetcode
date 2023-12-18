class Solution:
    def convert(self, s: str, numRows: int) -> str:
        convert = [[] for _ in range(numRows)]
        zig = 0
        flag = True # true: down, false: up
        for c in s:
            convert[zig].append(c)
            if flag and zig < numRows - 1:
                zig += 1
            elif flag and zig == numRows - 1:
                zig -= 1
                flag = False
            elif not flag and zig > 0:
                zig -= 1
            elif not flag and zig == 0:
                zig += 1
                flag = True

        flattened_convert = [item for sublist in convert for item in sublist] # thing for i in list for j in i 
        return ''.join(flattened_convert)
        