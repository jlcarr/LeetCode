class Solution:
    def minimizeXor(self, num1: int, num2: int) -> int:
        # get bits
        weight = 0
        while num2:
            weight += num2 % 2
            num2 = num2 // 2
        
        # to bits
        bits = []
        while num1:
            bits.append(num1 % 2)
            num1 = num1 // 2
        bits = bits[::-1]
        n = len(bits)
        #print('bits', bits)
        
        # if we have less, than we might as well assign all 1s as low as possible
        if n <= weight:
            return 2**weight - 1
        
        result = [0] * n
        # first assign to all 1s in num1
        for i in range(n):
            #print(result)
            if weight == 0:
                break
            if bits[i]:
                result[i] = 1
                weight -= 1
        
        #print("assign up")
        # assign remaining ones up from the bottom
        for i in range(n-1, -1, -1):
            #print(result)
            if weight == 0:
                break
            if result[i] == 0:
                result[i] = 1
                weight -= 1
            
        #print('fin', result)
        # build up the result
        res = 0
        for i in result:
            res *= 2
            if i:
                res += 1
        return res
    
    # 11001
    # 1001000
    # weight = 2
        
