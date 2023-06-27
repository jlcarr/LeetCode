class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        while n not in seen:
            seen.add(n)
            new_n = 0
            while n:
                new_n += (n%10) * (n%10)
                n //= 10 
            n = new_n
        return n == 1

