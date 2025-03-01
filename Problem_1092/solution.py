from functools import cache
class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        @cache
        def rec(i1, i2):
            if i1 == len(str1):
                return len(str2[i2:])
            if i2 == len(str2):
                return len(str1[i1:])
            if str1[i1] == str2[i2]:
                return 1 + rec(i1+1, i2+1)
            result1 = 1 + rec(i1+1, i2)
            result2 = 1 + rec(i1, i2+1)
            if result1 < result2:
                return result1
            return result2

        rec(0,0)

        result = []
        i1,i2 = 0,0
        while i1 < len(str1) and i2 < len(str2):
            if str1[i1] == str2[i2]:
                result.append(str1[i1])
                i1 += 1
                i2 += 1
            else:
                if rec(i1+1, i2) < rec(i1, i2+1):
                    result.append(str1[i1])
                    i1 += 1
                else:
                    result.append(str2[i2])
                    i2 += 1

        if i1 == len(str1):
            return ''.join(result) + str2[i2:]
        return ''.join(result) + str1[i1:]
