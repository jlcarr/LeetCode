class Solution:
    def reverse(self, x: int) -> int:
        sign = 1
        if x < 0:
            sign = -1
            x = -x
        result = 0
        while x:
            digit = x%10
            x //= 10
            if result > 2**31//10 \
                or 10*result > 2**31 - digit - (sign+1)//2:
                return 0
            result *= 10
            result += digit
        result *= sign
        return result
