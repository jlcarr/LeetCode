class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        result = ''
        zeroed = False
        for b1,b2 in zip(f"{left:031b}", f"{right:031b}"):
            #print(b1,b2)
            zeroed |= b1 != b2
            if zeroed:
                result += '0'
                continue
            result += b1
        #print(f"{left:031b}")
        #print(f"{right:031b}")
        #print(result)
        return int(result,2)
