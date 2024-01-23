class Solution:
    def maxLength(self, arr: List[str]) -> int:
        # remove arr[i] that have duplicates because those can never be included in the correct answer:
        arr = [s for s in arr if len(s) == len(set(s))]
        self.res = 0

        def dfs(visited, curr_length, i):
            if i == len(arr):
                self.res = max(self.res, curr_length)
                return

            # include (if it does not have duplicates) --> include by deleting duplicates do not need to be checked as iterate every start point outside of dfs
            if not (visited & set(arr[i])): # if new set (intersection between the sets) is not empty == true
                dfs(visited | set(arr[i]), curr_length + len(arr[i]), i + 1)
            
            # exclude
            dfs(visited, curr_length, i + 1)
        

        dfs(set(), 0, 0)
        return self.res
