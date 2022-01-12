class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        def eval(a, b, op):
            if op == "+":
                return a + b
            elif op == "-":
                return a - b
            elif op == "*":
                return a * b
            else:
                return int(a / b)
            
        stack = []
        
        for t in tokens:
            if t in "+-*/":
                b, a = stack.pop(), stack.pop()
                stack.append(eval(a, b, t))
            else:
                stack.append(int(t))
                
        return stack[0]
