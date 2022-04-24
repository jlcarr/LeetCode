class Solution:
    def convert(self, s: str, numRows: int) -> str:
        s = list(enumerate(s))
        
        block_size = numRows + max(0, numRows-2)
        numCols = len(s) // block_size + 1
        def num_func(s):
            block = s[0] // block_size
            block_pos = s[0] % block_size
            if block_pos < numRows:
                return 2*numCols*block_pos + 2*block
            return 2*numCols*(numRows-1-(block_pos+1-numRows)) + 2*block+1

        s = sorted(s, key=num_func)
        return ''.join(map(lambda c:c[1], s))
