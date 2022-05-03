class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"
        result = ""
        streak = 0
        streak_val = None
        for s in self.countAndSay(n-1):
            if not streak_val:
                streak_val = s
                streak += 1
            elif streak_val == s:
                streak += 1
            elif streak_val != s:
                result += str(streak) + str(streak_val)
                streak_val = s
                streak = 1
        result += str(streak) + str(streak_val)
        return result
