class Solution:
    def maxHeightOfTriangle(self, red: int, blue: int) -> int:
        result = 0
        tred = red
        tblue = blue
        for i in range(1,100):
            if i % 2 == 1:
                if i > red:
                    break
                red -= i
                result += 1
            else:
                if i > blue:
                    break
                blue -= i
                result += 1
        presult = result
        result = 0
        red = tred
        blue = tblue
        for i in range(1,100):
            if i % 2 == 0:
                if i > red:
                    break
                red -= i
                result += 1
            else:
                if i > blue:
                    break
                blue -= i
                result += 1
        return max(result, presult)
