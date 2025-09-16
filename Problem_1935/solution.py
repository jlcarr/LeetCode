class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        return sum(not bool(set(w) & set(brokenLetters)) for w in text.split())
