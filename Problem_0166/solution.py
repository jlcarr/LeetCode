class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        if numerator == 0:
            return '0'
        neg = (numerator < 0) ^ (denominator < 0)
        #print(neg)
        numerator, denominator = abs(numerator), abs(denominator)
        whole = numerator // denominator
        numerator = numerator % denominator
        rems = []
        rem_set = set([0])
        fract = []
        while numerator not in rem_set:
            rem_set.add(numerator)
            rems.append(numerator)
            numerator *= 10
            fract.append(numerator // denominator)
            numerator = numerator % denominator
        result = str(whole)
        if neg:
            result = '-'+result
        if not fract:
            return result
        result += '.'
        result += ''.join([str(dig) if r != numerator else '('+str(dig) for dig,r in zip(fract,rems)])
        if numerator in rems:
            result += ')'
        return result

