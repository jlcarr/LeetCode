class Solution:
    def tribonacci(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1:
            return 1
        t0 = 0
        t1 = 1
        t2 = 1
        for i in range(n-2):
            t2, t1, t0 = t2+t1+t0, t2, t1
        
        return t2
