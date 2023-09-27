class Solution:
    def decodeAtIndex(self, s: str, k: int) -> str:
        l = 0
        c_stack = []
        for c in s:
            if c.isalpha():
                l += 1
            else:
                l *= int(c)
            c_stack.append(c)
            if l >= k:
                break
        #print(l, c_stack)

        k -= 1
        while c_stack:
            if k == l-1:
                while not c_stack[-1].isalpha():
                    c_stack.pop()
                return c_stack[-1]
            while c_stack and c_stack[-1].isalpha() and l-1 > k:
                c_stack.pop()
                l -= 1
            while c_stack and c_stack[-1].isdigit() and l-1 > k:
                l //= int(c_stack.pop())
                k %= l
        
        return s[0]
