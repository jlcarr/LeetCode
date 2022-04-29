class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        sign = (dividend < 0)  ^ (divisor < 0)
        dividend, divisor = abs(dividend), abs(divisor)
        
        result = 0
        while dividend >= divisor:
            # compute power of 2
            bin_mul = divisor
            mul_count = 1
            while bin_mul + bin_mul <= dividend:
                bin_mul = bin_mul + bin_mul
                mul_count += mul_count
            # remove that power of 2
            dividend -= bin_mul
            result += mul_count
            
        if sign:
            return -result
        return min(result, 2147483647)
