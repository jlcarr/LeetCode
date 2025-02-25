class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        result = 0
        acc = 0
        odds = 0
        for i,v in enumerate(arr):
            acc ^= 1 & v
            #print(i,v,acc,odds, result)
            result += i+1-odds if acc else odds
            result %= 10**9 + 7
            odds += acc
            
        return result
