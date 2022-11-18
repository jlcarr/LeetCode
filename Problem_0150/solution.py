class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for tok in tokens:
            #print(tok, stack)
            if tok == '+':
                in1 = stack.pop()
                in2 = stack.pop()
                stack.append(in2+in1)
            elif tok == '-':
                in1 = stack.pop()
                in2 = stack.pop()
                stack.append(in2-in1)
            elif tok == '*':
                in1 = stack.pop()
                in2 = stack.pop()
                stack.append(in2*in1)
            elif tok == '/':
                in1 = stack.pop()
                in2 = stack.pop()
                stack.append(int(in2/in1))
            else:
                stack.append(int(tok))
        return str(stack[0])
