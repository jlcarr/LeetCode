class Solution:
    def alternateDigitSum(self, n: int) -> int:
        digs = []
        while n:
            digs.append(n%10)
            n //= 10
        digs = digs[::-1]
        return sum([n if i%2 == 0 else -n for i,n in enumerate(digs)])
