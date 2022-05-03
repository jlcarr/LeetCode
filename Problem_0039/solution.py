import functools
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        @lru_cache()
        def dp(start, target):
            result = []
            for i,n in enumerate(candidates[start:]):
                if n == target:
                    result.append([n])
                if n < target:
                    temp = dp(start+i, target-n)
                    result += [v+[n] for v in temp]
            return result
        return dp(0, target)
                    
