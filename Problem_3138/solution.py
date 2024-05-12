import math
from collections import Counter
class Solution:
    def minAnagramLength(self, s: str) -> int:
        # get all divisors
        n = len(s)
        root = int(math.sqrt(n))
        divisors = []
        for i in range(1,root+1):
            if n % i == 0:
                divisors.append(i)
                divisors.append(n//i)
        divisors.sort()
        # Try all slice sizes
        for div in divisors:
            failed = False
            c = Counter(s[:div])
            for i in range(n//div):
                if Counter(s[i*div:(i+1)*div]) != c:
                    failed = True
                    break
            if not failed:
                return div
        return n
