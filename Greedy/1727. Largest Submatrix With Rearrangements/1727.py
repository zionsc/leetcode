class Solution:
    def largestSubmatrix(self, matrix: List[List[int]]) -> int:
        if not matrix or not matrix[0]:
            return 0

        # Preprocess the Matrix
        for i in range(1, len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 1:
                    matrix[i][j] += matrix[i - 1][j]
        print(matrix)

        max_area = 0
        # Calculate Maximum Area
        for row in matrix:
            row.sort(reverse=True)
            print(matrix)
            for i in range(len(row)):
                max_area = max(max_area, row[i] * (i + 1))

        return max_area
    
#Preprocessing and Sorting:
# The preprocessing step changes each cell in the matrix to represent the number of consecutive 1s above it, including itself.
# Sorting each row in descending order rearranges these counts so that the larger counts are on the left.
# Understanding the Sorted Row:
# After sorting, each cell in a row tells you the maximum height of a rectangle (submatrix of 1s) that can be formed ending at that cell.