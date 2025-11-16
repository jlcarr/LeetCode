class Solution:
    def numSub(self, s: str) -> int:
        result = 0

        streak = 0
        for c in s+'0':
            if c == '0':
                # pairs + singles = nC2 + n
                result += streak*(streak-1)//2 + streak 
                streak = 0
            else:
                streak += 1

        return result % (10**9 + 7)
