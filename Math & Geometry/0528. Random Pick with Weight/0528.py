class Solution:

    def __init__(self, w: List[int]):
        self.w = w
        total = sum(w)
        length = len(w)
        self.lst = []

        for i in range(len(w)):
            num_times = 10000 * (w[i] / total)
            for j in range(int(num_times)):
                self.lst.append(i)

    def pickIndex(self) -> int:
        return random.choice(self.lst)
        
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()