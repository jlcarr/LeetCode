class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        result = 0
        l = len(arr)
        for i in range(l):
            for j in range(i+1,l):
                for k in range(j+1,l):
                    if abs(arr[i]-arr[j]) <= a \
                        and abs(arr[j]-arr[k]) <= b \
                        and abs(arr[i]-arr[k]) <= c:
                        result += 1
        return result
