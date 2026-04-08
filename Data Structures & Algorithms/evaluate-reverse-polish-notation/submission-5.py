class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        print(6//(-12))
        for token in tokens:
            if token == '+':
                a2 = stack.pop()
                a1 = stack.pop()
                res = a1 + a2
                stack.append(res)
            elif token == '-':
                a2 = stack.pop()
                a1 = stack.pop()
                res = a1 - a2
                stack.append(res)
            elif token == '*':
                a2 = stack.pop()
                a1 = stack.pop()
                res = a1 * a2
                stack.append(res)
            elif token == '/':
                a2 = stack.pop()
                a1 = stack.pop()
                res = int(a1 / a2)
                stack.append(res)
            else:
                stack.append(int(token))
            print(stack)
        return stack.pop()