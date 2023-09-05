class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        result = 0
        for i in range(low, high+1):
            i_str = str(i)
            n = len(i_str)
            if n % 2 == 0:
                if sum([int(c) for c in i_str[:n//2]]) == sum([int(c) for c in i_str[n//2:]]):
                    result += 1
        return result
