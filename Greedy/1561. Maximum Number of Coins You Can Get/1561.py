# class Solution:
#     def maxCoins(self, piles: List[int]) -> int:
#         piles.sort()
#         res = 0
#         while piles:
#             piles.pop()
#             res += piles.pop()
#             piles.pop(0)
#         return res
class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort(reverse=True)
        # because len(piles) // 3 rounds!!! so :-len(piles)//3 is are the ones that the bob dude picks
        return sum(piles[1:-len(piles)//3:2])