class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        invorder = {c:i for i,c in enumerate(order)}
        words = [[invorder[c] for c in w] for w in words]
        return words == sorted(words)

