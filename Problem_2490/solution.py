class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        sentence = sentence.split(' ')
        p = sentence[-1][-1]
        for w in sentence:
            if w[0] != p:
                return False
            p = w[-1]
        return True
