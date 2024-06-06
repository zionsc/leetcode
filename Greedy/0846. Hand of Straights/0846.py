class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        n = len(hand)
        
        if n % groupSize != 0:
            return False

        freq = Counter(hand)
        sortedNums = sorted(freq.keys())

        for num in sortedNums:
            if freq[num] > 0:
                numCount = freq[num]
                for i in range(num, num + groupSize):
                    if freq[i] < numCount:
                        return False
                    freq[i] -= numCount

        return True