class Solution:
    romans = [
        (1, 'I'),
        (5, 'V'),
        (10, 'X'),
        (50, 'L'),
        (100, 'C'),
        (500, 'D'),
        (1000, 'M')
    ][::-1]
    def intToRoman(self, num: int) -> str:
        result = ''
        for i,(nu_val, numeral) in enumerate(self.romans):
            if num >= nu_val:
                result += numeral * (num//nu_val)
                num %= nu_val
            if numeral != 'I':
                pre_nu_val, pre_numeral = self.romans[i + 1 + int(i%2==0)]
                if num >= nu_val - pre_nu_val:
                    result += pre_numeral + numeral
                    num %= pre_nu_val
        return result
