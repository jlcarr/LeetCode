class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        result  = set()
        for i,w1 in enumerate(words):
            for j,w2 in enumerate(words):
                if i != j and w1 in w2:
                    result.add(w1)
        return list(result)
