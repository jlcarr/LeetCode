from functools import cache
class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        @cache
        def rec(pos, M, turn):
            if pos >= len(piles):
                return 0

            objective = max if turn else min

            X = 1
            stones = objective(0, piles[pos+ X-1])
            result = stones + rec(pos+ X, max(M, X), not turn)

            for X in range(2, 2*M+1):
                if pos+X > len(piles):
                    break
                stones += objective(0, piles[pos+X-1])
                result = objective(result, stones+rec(pos+ X, max(M, X), not turn))

            return result

        return rec(0, 1, True)
