class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        ans = []
        for i,rows in enumerate(nums):
            for j,val in enumerate(nums[i]):
                if len(ans) <= i + j:
                    ans.append([])
                ans[i + j].append(val)

        res = []
        for row in ans:
            res += reversed(row)
        return res
        



        # res = defaultdict(deque)
        # for i, row in enumerate(nums):
        #     for j, val in enumerate(nums[i]):
        #         res[i + j].appendleft(val)

        # return chain(*res.values()) # * --> unpacks each deque from the hash map into its own individual deque --> map(dq1, dq2, dq3..) etc --> dq1, dq2, dq3. chain --> makes them into one iterative chain object --> can make it into list(chain(*res.values())) --> like that 



        # def custom_key(item):
        #     i_plus_j, num, i = item
        #     return (-i_plus_j, i)

        # sorted_arr = []
        # res = []
        # for i in range(len(nums)):
        #     for j in range(len(nums[i])):
        #         sorted_arr.append((i + j, nums[i][j], i))
        #         # heapq.heappush(min_heap, (i + j, nums[i][j]))
        
        # sorted_arr = sorted(sorted_arr, key=custom_key)
        # for i in range(len(sorted_arr) - 1, -1, -1):
        #     res.append(sorted_arr[i][1])
        # print(sorted_arr)
        # return res
