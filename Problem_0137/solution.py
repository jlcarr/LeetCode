class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        digs = [0]*32
        sign = 0
        for n in nums:
            if n < 0:
                sign = (sign + 1) % 3
                n = -n
            for i in range(32):
                print(i)
                if n == 0:
                    break
                if n % 2 == 1:
                    digs[i] = (digs[i] + 1) % 3
                n //= 2

        result = sum([1 << i for i in range(32) if digs[i]])
        if sign:
            result = -result
        return result
