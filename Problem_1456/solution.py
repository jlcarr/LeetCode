class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        s = [c in 'aeiou' for c in s]
        count = sum(s[:k])
        result = count
        for i in range(k,len(s)):
            count += s[i] - s[i-k]
            result = max(result, count)
        return result
