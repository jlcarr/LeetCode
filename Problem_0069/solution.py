class Solution:
    def mySqrt(self, x: int) -> int:
        # solve ans*ans - x = 0
        if x == 0:
            return 0
        ans = x
        while True:
            diff = (ans*ans-x)/(2*ans)
            ans -= diff
            if abs(diff) < 1:
                return int(ans)
