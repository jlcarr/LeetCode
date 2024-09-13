class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        cumArr = [0]
        for i in arr:
            cumArr.append(cumArr[-1] ^ i)
        
        return [cumArr[r+1] ^ cumArr[l] for l,r in queries]

