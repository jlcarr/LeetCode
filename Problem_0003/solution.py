class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        result = 0
        start = 0
        pos = dict()
        for i,c in enumerate(s):
            if c in pos and pos[c] >= start:
                result = max(result, i-start)
                start = pos[c]+1
            pos[c] = i
        result = max(result,len(s)-start)
        return result
