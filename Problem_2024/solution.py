from collections import deque
class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        n = len(answerKey)
        arrays = [[ans == v for ans in answerKey] for v in 'TF']
        result = 0
        for arr in arrays:
            q = deque([])
            kcurr = k
            last_index = 0
            for i in range(n):
                if not arr[i]:
                    if kcurr == 0:
                        last_index = q.pop() +1
                        kcurr += 1
                    kcurr -= 1
                    q.appendleft(i)
                result = max(result, i - last_index + 1)
        return result
