class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        rem = time % (2 * n - 2)
        if rem < n:
            return rem + 1
        return 2 * n - 1 - rem
