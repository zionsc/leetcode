class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        res=deque()

        for card in reversed(sorted(deck)):
            res.rotate(1) # move one from back to the front
            res.appendleft(card)

        return res