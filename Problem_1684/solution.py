class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        c = set(allowed)
        return sum(not (set(w)-c) for w in words)
