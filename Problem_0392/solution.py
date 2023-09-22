class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if not s:
            return True
        curr = 0
        for c in t:
            if c == s[curr]:
                curr += 1
                if curr == len(s):
                    return True
        return False
