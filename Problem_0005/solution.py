class Solution:
    def longestPalindrome(self, s: str) -> str:
        result = s[0]
        for i,c in enumerate(s):
            j = 1
            temp = s[i]
            while i-j >= 0 and i+j < len(s) and s[i-j] == s[i+j]:
                temp = s[i-j] + temp + s[i+j]
                j+=1
            if len(temp) > len(result):
                result = temp
                
            j = 1
            temp = ''
            while i-j >= 0 and i+j-1 < len(s) and s[i-j] == s[i+j-1]:
                temp = s[i-j] + temp + s[i+j-1]
                j+=1
            if len(temp) > len(result):
                result = temp
        return result
