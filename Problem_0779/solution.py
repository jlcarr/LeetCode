class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        # 0
        # 01
        # 0110
        # 01101001
        # 0110100110010110
        # 01101001100101101001011001101001
        return f"{k-1:b}".count('1') % 2
