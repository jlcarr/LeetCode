class Solution:
    def compressedString(self, word: str) -> str:
        comp = []
        prev = ''
        prevlen = 0
        for c in word+' ':
            if prev and prev != c or prevlen == 9:
                comp.append(str(prevlen))
                comp.append(prev)
                prevlen = 0
            prevlen += 1
            prev = c
        return ''.join(comp)
