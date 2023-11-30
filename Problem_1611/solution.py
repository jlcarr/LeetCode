class Solution:
    def minimumOneBitOperations(self, n: int) -> int:
        mask = n
        while mask:
            mask >>= 1
            n ^= mask
        return n
