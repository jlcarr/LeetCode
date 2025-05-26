class Solution:
    def getWordsInLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        prevs = []
        scores = []
        for i,(g,w) in enumerate(zip(groups, words)):
            jmax = -1
            curr = 0
            for j,s in enumerate(scores):
                if s > curr and groups[j] != g \
                    and len(words[j]) == len(w) and sum(c1 != c2 for c1,c2 in zip(w, words[j])) == 1:
                    curr = s
                    jmax = j
            prevs.append(jmax)
            scores.append(curr+1)
        imax = max(range(len(scores)), key=lambda i: scores[i])
        #print(prevs)
        #print(scores)
        #print(imax)
        result = []
        while imax != -1:
            result.append(words[imax])
            imax = prevs[imax]
        return result[::-1]

