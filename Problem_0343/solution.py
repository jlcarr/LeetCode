class Solution:
    def integerBreak(self, n: int) -> int:
        result = 0
        for k in range(2,n+1):
            div = n // k
            rem = n % k
            sub_result = div ** (k - rem) * (div+1) ** rem
            result = max(result, sub_result)
            #print(k, div, rem, sub_result)
        return result
