class Solution:
    def parseBoolExpr(self, expression: str) -> bool:
        op_stack = []
        num_stack = []
        for c in expression:
            if c == 't':
                num_stack.append(True)
            if c == 'f':
                num_stack.append(False)
            if c in '!&|':
                op_stack.append(c)
            if c == '(':
                num_stack.append('(')
            if c == ')':
                if op_stack[-1] == '!':
                    v = not num_stack.pop()
                if op_stack[-1] == '&':
                    v = num_stack.pop()
                    while num_stack[-1] != '(':
                        v &= num_stack.pop()
                if op_stack[-1] == '|':
                    v = num_stack.pop()
                    while num_stack[-1] != '(':
                        v |= num_stack.pop()
                num_stack.pop()
                num_stack.append(v)
                op_stack.pop()
        return num_stack.pop()
