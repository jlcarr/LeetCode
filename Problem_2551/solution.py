class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:
        if k == 1:
            return 0

        n = len(weights)

        pairs = []
        for i in range(n-1):
            pairs.append(weights[i]+weights[i+1])
        pairs.sort()

        return sum(pairs[-k+1:]) - sum(pairs[:k-1])
