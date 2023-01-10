class Solution:
    def trailingZeroes(self, n: int) -> int:
        fives = 0
        fact = 5
        while n // fact > 0:
            fives += n // fact
            fact *= 5

        twos = 0
        fact = 2
        while n // fact > 0:
            twos += n // fact
            fact *= 2
        
        return min(twos, fives)
