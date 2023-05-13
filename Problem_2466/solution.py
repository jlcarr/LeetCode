class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        comb = [0] * (high+1)
        comb[0] = 1
        for i in range(high+1):
            if i + zero < high+1:
                comb[i+zero] += comb[i]
                comb[i+zero] %= 10**9 + 7
            if i + one < high+1:
                comb[i+one] += comb[i]
                comb[i+one] %= 10**9 + 7
        return sum(comb[i] for i in range(low, high+1)) % (10**9 + 7)
