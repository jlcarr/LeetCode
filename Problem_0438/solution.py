from collections import Counter
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        lp, ls = len(p), len(s)
        if ls < lp:
            return []
        p = Counter(p)
        window = Counter(s[:lp])
        result = []
        if window == p:
                result.append(0)
        i = 0
        while i+lp < ls:
            window[s[i]] -= 1
            window[s[i+lp]] += 1
            i += 1
            if window == p:
                    result.append(i)

        return result
