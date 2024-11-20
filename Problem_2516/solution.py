class Solution:
    def takeCharacters(self, s: str, k: int) -> int:
        if k == 0:
            return 0

        abc = [0,0,0]
        for c in 'abc':
            ia = ord(c)-ord('a')
            abc[ia] = k-s.count(c) 

        if any(count > 0 for count in abc):
            return -1

        result = len(s)
        j = 0
        for i,c in enumerate(s):
            ia = ord(c)-ord('a')
            abc[ia] += 1
            while abc[ia] > 0:
                ja = ord(s[j])-ord('a')
                abc[ja] -= 1
                j += 1
            result = min(result, len(s) - (i+1-j))
        return result
