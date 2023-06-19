class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        result = 0
        acc = 0
        for g in gain:
            acc += g
            result = max(result, acc)
        return result
