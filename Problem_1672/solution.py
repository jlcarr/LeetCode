class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        accounts = list(map(sum, accounts))
        return max(accounts)
