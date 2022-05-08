class Solution:
    phi = (1+5**0.5)/2
    def climbStairs(self, n: int) -> int:
        return round((self.phi**(n+1) - (-self.phi)**(-n-1))/(5**0.5))
        
