class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        # go up storing number of flips required to make the rest all 1s or 0s
        sum0 = sum([int(c=='0') for c in s])
        result = sum0
        acc0 = 0
        acc1 = 0
        for c in s:
            # turn prev and curr 0s, turn next 1s
            acc0 += int(c=='0')
            acc1 += int(c=='1')
            result = min(result, (acc1) + (sum0 - acc0))
        return result
