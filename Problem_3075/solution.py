class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        return sum(max(v-i,0) for i,v in enumerate(sorted(happiness, reverse=True)[:k]))
