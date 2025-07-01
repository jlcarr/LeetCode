class Solution:
    def possibleStringCount(self, word: str) -> int:
        result = 1
        i = 0
        j = 0
        while j < len(word):
            while j < len(word) and word[i] == word[j]:
                j += 1
            result += j - i - 1
            i = j
        return result
