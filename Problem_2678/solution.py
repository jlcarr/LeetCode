class Solution:
    def countSeniors(self, details: List[str]) -> int:
        return sum(d[11:13] > '60' for d in details)
