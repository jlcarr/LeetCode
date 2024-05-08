class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        order = {0:"Gold Medal", 1:"Silver Medal", 2:"Bronze Medal",}
        indices = {s:order.get(i, str(i+1)) for i,s in enumerate(sorted(score, reverse=True))}
        return [indices[s] for s in score]

