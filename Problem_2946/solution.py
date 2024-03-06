class Solution:
    def areSimilar(self, mat: List[List[int]], k: int) -> bool:
        n = len(mat[0])
        k = k % n
        for i,row in enumerate(mat):
            if i % 2 == 1:
                if any(row[i] != row[((i+n-k)%n)] for i in range(n)):
                    return False
            else:
                if any(row[i] != row[(i+k)%n]  for i in range(n)):
                    return False
        return True
