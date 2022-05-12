from functools import cache
class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        if len(s) < 4:
            return []
        @cache
        def dp(i, rem):
            print(i, rem)
            if rem == 1:
                if (s[i] != '0' or i == len(s)-1) and int(s[i:]) <= 255:
                    return [ s[i:] ]
                else:
                    return []
            if s[i] == '0':
                sub_results = dp(i+1, rem-1)
                return ['0.'+r for r in sub_results]
            result = []
            for j in range(i+1, len(s)+1-rem+1):
                v = s[i:j]
                if int(v) > 255:
                    break
                sub_results = dp(j, rem-1)
                result += [v+'.'+r for r in sub_results]
            return result
        return dp(0, 4)
