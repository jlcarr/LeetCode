class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        rem = set()
        stack = []
        for i,c in enumerate(s):
            if c == '(':
                stack.append(i)
            if c == ')':
                if not stack:
                    rem.add(i)
                else:
                    stack.pop()
        rem |= set(stack)

        return ''.join(c for i,c in enumerate(s) if i not in rem)
