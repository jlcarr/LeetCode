from functools import cache
class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        max_scores= [0]*(max(ages))

        scores_ages = sorted(list(zip(scores,ages)))
        for score,age in scores_ages:
            max_scores[age-1] = score + max(max_scores[:age])
        
        return max(max_scores)
