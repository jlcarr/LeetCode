class Solution:
    def areSentencesSimilar(self, sentence1: str, sentence2: str) -> bool:
        sentence1 = sentence1.split()
        sentence2 = sentence2.split()
        if len(sentence1) == len(sentence2):
            return sentence1 == sentence2
        if len(sentence1) > len(sentence2):
            sentence1, sentence2 = sentence2, sentence1
        
        seq_inserted = False
        i2 = 0
        for i1, w1 in enumerate(sentence1):
            if w1 != sentence2[i2]:
                i2 += len(sentence2) - len(sentence1)
                if seq_inserted or w1 != sentence2[i2]:
                    return False
                seq_inserted = True
            i2 += 1
        return True
