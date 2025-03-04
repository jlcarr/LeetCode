class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        # This is the same thing as no 2s in the base 3
        while n:
            if n % 3 == 2:
                return False
            n //= 3
        return True
