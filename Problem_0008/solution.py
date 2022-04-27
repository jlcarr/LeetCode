import re
class Solution:
    def myAtoi(self, s: str) -> int:
        v = re.match(r'^\s*([\+\-]?)(\d+)', s)
        if not v:
            return 0
        sign,mantissa = v.groups()
        if not mantissa:
            return 0
        result = int(mantissa)
        if sign == '-':
            result *= -1
            if result < -2**31:
                result = -2**31
        else:
            if result > 2**31-1:
                result = 2**31-1
        return result
        
