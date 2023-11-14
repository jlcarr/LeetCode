class Solution:
    def sortVowels(self, s: str) -> str:
        v = [c for c in s if c.lower() in 'aeiou']
        v.sort(key=lambda c: ord(c), reverse=True)
        return ''.join(v.pop() if c.lower() in 'aeiou' else c for c in s)
