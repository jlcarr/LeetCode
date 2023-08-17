class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m,n = len(mat), len(mat[0])
        result = [[0 for j in range(n)] for i in range(m)]
        layer = set()
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    layer.add((i,j))
        
        nlayer = 1
        searched = set([i for i in layer])
        while layer:
            new_layer = set()
            while layer:
                ip,jp = layer.pop()
                for i,j in [(ip+1,jp),(ip-1,jp),(ip,jp+1),(ip,jp-1)]:
                    if (i,j) not in searched and (0 <= i < m) and (0 <= j < n):
                        searched.add((i,j))
                        new_layer.add((i,j))
                        result[i][j] = nlayer
            layer = new_layer
            nlayer += 1
        
        return result
