class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        for layer in range(n//2):
            #print("layer", layer)
            for i in range(n-2*layer-1):
                #print("index", i)
                #print(matrix[layer][layer+i], matrix[layer+i][-layer-1], matrix[-layer-1][-layer-1-i], matrix[-layer-1-i][layer])
                # top-left [layer][layer+i]
                # top-right [layer+i][-layer-1]
                # bottom-right [-layer-1][-layer-1-i]
                # bottom-left [-layer-1-i][layer]
                
                matrix[layer+i][-layer-1], matrix[-layer-1][-layer-1-i], \
                matrix[-layer-1-i][layer], matrix[layer][layer+i] \
                    = matrix[layer][layer+i], matrix[layer+i][-layer-1], \
                   matrix[-layer-1][-layer-1-i], matrix[-layer-1-i][layer]
                
