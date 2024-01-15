class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        answers = [[],[]]
        loser_map = defaultdict(int)

        for w,l in matches:
            loser_map[l] += 1
            loser_map[w] = loser_map[w]
        
        for i,v in loser_map.items():
            if v == 0:
                answers[0].append(i)
            elif v == 1:
                answers[1].append(i)
        
        answers[0].sort()
        answers[1].sort()
        return answers
