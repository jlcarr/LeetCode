import math
class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        for a in range(0,1+int(math.ceil(math.sqrt(c/2)))):
            if c - a*a < 0:
                continue
            b = int(round(math.sqrt(c-a*a)))
            if a*a + b*b == c:
                return True
        return False
