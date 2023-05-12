class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        n = len(questions)
        result = 0
        scores = [0] * n
        for i,(p,b) in enumerate(questions):
            if i + 1 + b < n:
                scores[i+1+b] = max(scores[i+1+b], p+scores[i])
            else:
                result = max(result, p+scores[i])
            if i+1 < n:
                scores[i+1] = max(scores[i+1], scores[i])
        return result
