class Solution:
    def beautifulSubsets(self, nums: List[int], k: int) -> int:
        self.res=0
        n=len(nums)
        def backtrack(idx: int, currSubset: List[int], used: defaultdict(int)) -> None:
            if idx == n:
                self.res+=1
                return
            
            if used[nums[idx] - k] == 0 and used[nums[idx] + k] == 0:
                currSubset.append(nums[idx])
                used[nums[idx]] += 1
                backtrack(idx + 1, currSubset, used)
                currSubset.pop()
                used[nums[idx]] -= 1
            backtrack(idx + 1, currSubset, used)
            
        
        backtrack(0, [], defaultdict(int))
        return self.res - 1
                        