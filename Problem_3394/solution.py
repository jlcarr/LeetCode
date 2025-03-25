class Solution:
    def checkValidCuts(self, n: int, rectangles: List[List[int]]) -> bool:
        # x
        gaps = 1 # end
        curr = -1 # start
        rectangles.sort(key=lambda x: x[0])
        for sx,sy,ex,ey in rectangles:
            if sx >= curr:
                gaps += 1
            curr = max(curr, ex)
        if gaps >= 4:
            return True
        # y 
        gaps = 1 # end
        curr = -1 # start
        rectangles.sort(key=lambda x: x[1])
        for sx,sy,ex,ey in rectangles:
            if sy >= curr:
                gaps += 1
            #print(gaps, curr, sx,sy,ex,ey)
            curr = max(curr, ey)
        #print(rectangles, gaps)
        if gaps >= 4:
            return True
        
        return False

