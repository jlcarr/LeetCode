from collections import Counter
class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        cs = Counter(chars)
        return sum(len(w) for w in words if Counter(w) <= cs)
