class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        k -= 1
        result = ""
        
        digits = list(map(str,range(1,n+1)))
        
        perm_base = 1
        for i in range(1,n):
            perm_base *= i
        
        for d in range(n-1,0,-1):
            #print('perm_base',perm_base)
            #print('d',d, 'k',k)
            i_digit = k // perm_base
            result += digits[i_digit]
            del digits[i_digit]
            
            k %= perm_base
            if d >0:
                perm_base //= d
        result += digits[0]
                
        return result
