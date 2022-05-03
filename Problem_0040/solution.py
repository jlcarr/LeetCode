from functools import lru_cache
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        @lru_cache()
        def dp(start, target):
            n = candidates[start]
            result = []
            # keep case
            # find end of streak
            streak_end = start
            while streak_end < len(candidates) and n == candidates[streak_end]:
                streak_end += 1
            # try adding duplicates
            new_target = target
            for i in range(start, streak_end):
                new_target -= n
                if new_target < 0:
                    break
                elif new_target == 0:
                    result.append([n]*(i+1-start))
                    break
                if streak_end < len(candidates):
                    temp = dp(streak_end, new_target)
                    result += [[n]*(i+1-start)+v for v in temp]
            #discard case
            if streak_end < len(candidates):
                result += dp(streak_end, target)
            return result

        candidates.sort()
        return dp(0, target)
