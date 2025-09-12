class Solution:
    def doesAliceWin(self, s: str) -> bool:
        # odd -> A win
        # even -> odd -> odd -> A win
        # 0 -> A lose
        # 1 -> 0 -> B lose
        return any(c in 'aeiou' for c in s)
