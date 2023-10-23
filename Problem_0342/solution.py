class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n < 0:
            return False
        binary = f"{n:b}"
        return (len(binary) % 2 == 1) and (binary.count('1') == 1)
