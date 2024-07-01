class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        odds = 0
        for i in arr:
            if i % 2:
                odds += 1
            else:
                odds = 0
            if odds >= 3:
                return True
        return False
