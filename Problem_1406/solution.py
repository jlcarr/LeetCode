from functools import cache
class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        @cache
        def rec(pos, turn):
            if pos == len(stoneValue):
                return 0
            result = None
            stones = 0
            for new_pos in range(pos,pos+3):
                if new_pos >= len(stoneValue):
                    break
                sub_result = rec(new_pos+1, not turn)
                if turn:
                    stones += stoneValue[new_pos]
                    if result is None:
                        result = stones+sub_result
                    result = max(result, stones+sub_result)
                else:
                    if result is None:
                        result = sub_result
                    result = min(result, sub_result)
            return result

        alice = rec(0, True)
        bob = sum(stoneValue) - alice
        if alice > bob:
            return "Alice"
        if bob > alice:
            return "Bob"
        return "Tie"
