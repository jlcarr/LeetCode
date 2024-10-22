class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        lookup = set()
        def rec(i=0):
            result = -len(s)
            if i == len(s):
                return 0
            for j in range(i+1,len(s)+1):
                substr = s[i:j]
                if substr not in lookup:
                    lookup.add(substr)
                    result = max(result, 1+rec(i=j))
                    lookup.remove(substr)
            return result
        return rec()
