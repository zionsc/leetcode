class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        tokens.sort()
        max_score = score = 0
        l,r = 0, len(tokens) - 1

        while l <= r:
            if power >= tokens[l]:
                power -= tokens[l]
                l += 1
                score += 1
                max_score = max(max_score, score)
            elif score > 0:
                power += tokens[r]
                score -= 1
                r -= 1
            else:
                break
            
        return max_score