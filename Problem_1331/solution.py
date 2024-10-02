class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        ranks = {v:i+1 for i,v in enumerate(sorted(set(arr)))}
        return list(map(ranks.get, arr))
