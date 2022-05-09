from functools import lru_cache
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        @lru_cache(maxsize=None)
        def rec(i,k):
            if k > n+1-i:
                return []
            if k == 1:
                return [[c] for c in range(i,n+1)]
            # case without
            result = rec(i+1, k)
            # case with
            sub_res = rec(i+1, k-1)
            sub_res = [[i]+c for c in sub_res]
            result += sub_res
            return result
            
        return rec(1,k)
