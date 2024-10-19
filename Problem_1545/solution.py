class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        l = 1
        for i in range(n-1):
            l = 2*l + 1
        
        k -= 1

        inverted = False
        for i in range(n-1):
            #print(n-i, k, inverted)
            l //= 2
            if k == l:
                return str(int(not inverted))
            if k > l:
                inverted = not inverted
                k -= l+1
                k = l - 1 - k
                #k = 2 * l - k
        
        return str(int(inverted))
