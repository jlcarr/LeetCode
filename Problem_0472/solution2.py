class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        words.sort(key=lambda w: len(w))
        self.found = set()
        def dfs(w, prev=False):
            #print(w, prev)
            if w == '' and prev:
                return True
            sub_w = ''
            for i in range(len(w)):
                sub_w += w[i]
                if sub_w in self.found:
                    if prev == False and i+1 == len(w):
                        continue
                    if dfs(w[i+1:], prev=True):
                        return True
            return False
            
        result = []
        for w in words:
            if dfs(w):
                result.append(w)
            self.found.add(w)
        #print(t)
        return result
