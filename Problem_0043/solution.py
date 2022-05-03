class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == '0' or num2 == '0':
            return '0'
        #perform the single-digit multiplications 
        results_strings = []
        for pos1,d1 in enumerate(num1[::-1]):
            d1 = ord(d1)-ord('0')
            carry = 0
            temp = "0"*pos1
            for pos2,d2 in enumerate(num2[::-1]):
                d2 = ord(d2)-ord('0')
                result = (d2*d1+carry)%10
                carry = (d2*d1+carry)//10
                temp += chr(result+ord('0'))
            if carry:
                temp += chr(carry+ord('0'))
            results_strings.append(temp)
        #print(results_strings)
        
        # perform the final addition
        carry = 0
        pos = 0
        done = False
        result = ''
        while not done:
            done = True
            for s in results_strings:
                if pos < len(s):
                    carry += ord(s[pos]) - ord('0')
                    done = False
            if done:
                break
            pos += 1
            result += chr(carry%10+ord('0'))
            carry = carry // 10
        while carry:
            result += chr(carry%10+ord('0'))
            carry = carry // 10
        return result[::-1]
        
