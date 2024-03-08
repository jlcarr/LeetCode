class Solution:
    def beautifulSubstrings(self, s: str, k: int) -> int:
        result = 0
        vowels = 0
        for r,ch in enumerate(s):
            if ch in 'aeiou':
                vowels += 1
            subvowels = vowels
            for l in range(r):
                length = r+1-l
                if 2*subvowels == length and (subvowels*subvowels)%k == 0:
                    #print(l,r)
                    result += 1
                if s[l] in 'aeiou':
                    subvowels -= 1
        return result
