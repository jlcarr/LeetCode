class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        if len(s) % 2:
            return False
        l_stack = []
        a_stack = []

        for i,(c,l) in enumerate(zip(s,locked)):
            if l == '0':
                a_stack.append(i)
            elif c == '(':
                l_stack.append(i)
            elif c == ')':
                if l_stack:
                    l_stack.pop()
                elif a_stack:
                    a_stack.pop()
                else:
                    return False
            else: # wrong turn
                return None
        while l_stack and a_stack and l_stack[-1] < a_stack[-1]:
            l_stack.pop()
            a_stack.pop()

        return not l_stack
