class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        t = list(reversed(t))
        for c in s:
            if c == t[-1]:
                t.pop()
                if not t:
                    break
        return len(t)
