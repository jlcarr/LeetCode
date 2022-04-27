class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        result = strs[0]
        for s in strs[1:]:
            for i in range(len(result)):
                if i >= len(s) or result[i] != s[i]:  
                    result = result[:i]
                    break
        return result
