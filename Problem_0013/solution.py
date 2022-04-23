class Solution:
    def romanToInt(self, s: str) -> int:
        val = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        result = 0
        while s:
            digit, s = s[0],s[1:]
            digit = val[digit]
            if s and val[s[0]] > digit:
                result -= digit
            else:
                result += digit
        return result
