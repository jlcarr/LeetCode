class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        l = len(arr)
        winner = 0
        challenger = 1
        count = 0
        while count < k and challenger < l:
            #print(winner, challenger, arr[winner], arr[challenger], count)
            if arr[winner] < arr[challenger]:
                winner = challenger
                count = 0
            count += 1
            challenger += 1
        return arr[winner]
