class Solution:
    def getSum(self, a: int, b: int) -> int:
        bit_mask = 0xFFFFFFFF
        while b:
            carry = (a & b)
            a = a ^ b
            b = carry << 1
            a, b = a&bit_mask, b&bit_mask
        return a if a <= 0x8FFFFFFF else ~(a ^ bit_mask)
