class Solution:
    def smallestRepunitDivByK(self, k: int) -> int:
        acc = 1
        for i in range(k):
            acc %= k
            if acc == 0:
                return i+1
            acc *= 10
            acc += 1
        return -1
