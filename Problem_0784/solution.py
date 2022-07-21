class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        result = ['']
        for i in range(len(s)):
            if s[i].upper() != s[i].lower():
                result = [string + s[i].upper() for string in result] \
                    + [string + s[i].lower() for string in result]
            else:
                result = [string + s[i] for string in result]
        return result
