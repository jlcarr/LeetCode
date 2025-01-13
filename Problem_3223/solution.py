from collections import Counter
class Solution:
    def minimumLength(self, s: str) -> int:
        # 12 (0)3->1, (1)4->2 (2)5->3, 6->
        return sum(2-(v%2) for v in Counter(s).values())
