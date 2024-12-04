class Solution:
    def canMakeSubsequence(self, str1: str, str2: str) -> bool:
        str2 = [ord(c)-ord('a') for c in str2][::-1]
        for c in str1:
            v = ord(c)-ord('a')
            if str2[-1] == v or str2[-1] == (v+1)%26:
                str2.pop()
                if not str2:
                    return True
        return False
