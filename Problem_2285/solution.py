class Solution:
    def maximumImportance(self, n: int, roads: List[List[int]]) -> int:
        degrees = [0]*n
        for e in roads:
            for i in e:
                degrees[i] += 1
        degrees.sort(reverse=True)
        result = 0
        for i,degree in enumerate(degrees):
            result += degree * (n-i)
            #print(i, degree, result)
        return result

