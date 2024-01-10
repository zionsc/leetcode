# """
# This is BinaryMatrix's API interface.
# You should not implement it, or speculate about its implementation
# """
#class BinaryMatrix(object):
#    def get(self, row: int, col: int) -> int:
#    def dimensions(self) -> list[]:

class Solution:
    def leftMostColumnWithOne(self, binaryMatrix: 'BinaryMatrix') -> int:
        rows,cols = binaryMatrix.dimensions()

        r,c = 0, cols - 1
        res = -1
        while r < rows and c >= 0:
            if binaryMatrix.get(r,c) == 1:
                res = c
                c -= 1
            else:
                r += 1
        return res
