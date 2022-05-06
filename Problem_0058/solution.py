class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.strip()
        l = 0
        for c in s:
            if c != ' ':
                l += 1
            else:
                l = 0
        return l
