class Solution:
    def minimumOperations(self, num: str) -> int:
        if len(num) == 0:
            return 0
        if len(num) == 1:
            if num == '0':
                return 0
            return 1
        if len(num) >= 2:
            if num[-2:] in ['00', '25', '50', '75']:
                return 0
            if len(num) == 2:
                if '0' in num:
                    return 1
                return 2
        
        num = list(num)
        
        result = len(num)
        
        # aim for 5 ending
        orig = num[:]
        while num and num[-1] != '5':
            num.pop()
        if num:
            num.pop()
            
        while len(num) > 0 and num[-1] not in ['2','7']:
            num.pop()
        
        if len(num) >= 1:
            result = min(result, len(orig) - (len(num)+1))
        
        
        # aim for 0 ending
        num = orig[:]
        while num and num[-1] != '0':
            num.pop()
        if num:
            num.pop()
            
        while len(num) > 0 and num[-1] not in ['0','5']:
            num.pop()
        
        if len(num) >= 1:
            result = min(result, len(orig) - (len(num)+1))
        
        #print(orig, num)
        if '0' in orig:
            result = min(result, len(orig)-1)
            
        return result
