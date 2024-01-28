class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        row,col = len(matrix),len(matrix[0])
        sub_sum = [[0] * col for _ in range(row)]

        for r in range(row):
            for c in range(col):
                top = sub_sum[r - 1][c] if r > 0 else 0
                left = sub_sum[r][c - 1] if c > 0 else 0 
                top_left = sub_sum[r - 1][c - 1] if min(r,c) > 0 else 0
                sub_sum[r][c] = matrix[r][c] + top + left - top_left
        
        res = 0
        for r_start in range(row):
            for r_end in range(r_start, row):
                count = defaultdict(int) # we want to initialize it for every row submatrices we consider
                # this is because we want to make sure individual cells can be connected 
                # smaller start-->end submatrices will all be considered in later iterations (bigger ones)
                count[0] = 1 # a sum of 0 has been seen once (since if we find a sum == target, then we need to add it to res)
                for c in range(col):
                    curr_sum = sub_sum[r_end][c] - (
                        sub_sum[r_start - 1][c] if r_start > 0 else 0
                    )
                    diff = curr_sum - target
                    res += count[diff]
                    count[curr_sum] += 1
        return res

