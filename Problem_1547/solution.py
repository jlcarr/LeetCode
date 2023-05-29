from functools import cache
class Solution:
    def minCost(self, n: int, cuts: List[int]) -> int:
        cuts.sort()
        ncuts = len(cuts)
        @cache
        def rec(il,ir):
            if il+1 == ir:
                return 0
            start = 0 if il == -1 else cuts[il]
            end = n if ir == ncuts else cuts[ir]
            result = None
            for i in range(il+1, ir):
                sub_result = end-start
                sub_result += rec(il, i)
                sub_result += rec(i, ir)
                if result is None or sub_result < result:
                    result = sub_result
            return result
        return rec(-1,ncuts)
