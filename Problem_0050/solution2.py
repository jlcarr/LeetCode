class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1.0
        if n < 0:
            return self.myPow(1/x, -n)
        if n%2:
            return x * self.myPow(x, n-1)
        x_pow = self.myPow(x, n//2)
        return x_pow*x_pow
