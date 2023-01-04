from collections import Counter
class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        tasks = Counter(tasks)
        result = 0
        for t,c in tasks.items():
            if c == 1:
                return -1
            if c%3 == 0:
                result += c//3
            elif c%3 == 1:
                result += c//3 + 1
            elif c%3 == 2:
                result += c//3 + 1
        return result
