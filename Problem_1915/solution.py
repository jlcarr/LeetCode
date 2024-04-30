class Solution:
    def wonderfulSubstrings(self, word: str) -> int:
        result = 0
        mask = 0
        counts = [0] * (1 << 10)
        counts[0] = 1

        for c in word:
            mask ^= 1 << (ord(c) - ord('a'))
            result += counts[mask]
            for i in range(10):
                result += counts[mask ^ (1 << i)]
            counts[mask] += 1
        return result
