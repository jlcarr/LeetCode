from collections import Counter
class Solution:
    def maxScoreWords(self, words: List[str], letters: List[str], score: List[int]) -> int:
        words = [Counter(w) for w in words]
        self.letters = Counter(letters)
        def backtrack(iw):
            if iw == len(words):
                return 0
            result = 0
            word = words[iw]
            if word <= self.letters:
                self.letters -= word
                result = sum(v * score[ord(k)-ord('a')] for k,v in word.items())
                result += backtrack(iw+1)
                self.letters += word
            return max(result, backtrack(iw+1))
        return backtrack(0)
