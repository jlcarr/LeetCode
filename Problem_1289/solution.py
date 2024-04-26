class Solution:
    def minFallingPathSum(self, grid: List[List[int]]) -> int:
        prev_imin, prev_vmin= -1, 0
        prev_ipmin, prev_vpmin = -1, 0
        for row in grid:
            imin, vmin = None, None
            ipmin, vpmin = None, None
            for i,v in enumerate(row):
                vv = v + (prev_vmin if i != prev_imin else prev_vpmin)
                if vmin is None:
                    imin, vmin = i, vv
                elif vpmin is None:
                    if vv <= vmin:
                        ipmin, vpmin = imin, vmin
                        imin, vmin = i, vv
                    else:
                        ipmin, vpmin = i, vv
                elif vv <= vmin:
                    ipmin, vpmin = imin, vmin
                    imin, vmin = i, vv
                elif vv <= vpmin:
                    ipmin, vpmin = i, vv
            prev_imin, prev_vmin= imin, vmin
            prev_ipmin, prev_vpmin = ipmin, vpmin
        
        return vmin
