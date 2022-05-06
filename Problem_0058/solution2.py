class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        i = 1
        result = 0
        while i <= len(s):
            if s[-i] != ' ':
                result += 1
            elif result != 0:
                return result
            i += 1
        return result
