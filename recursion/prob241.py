class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        
        def op(l, r, o):
            l, r = int(l), int(r)
            if o == "+":
                return l + r
            elif o == "-":
                return l - r
            else:
                return l * r
            
        def evaluate(exp):
            if "+" not in exp and "-" not in exp and "*" not in exp:
                return [int(exp)]
            
            ans = []
            for i in range(len(exp)):
                o = exp[i]
                if o in "+-*":
                    left = evaluate(exp[:i])
                    right = evaluate(exp[i+1:])
                    for l in left:
                        for r in right:
                            ans.append(op(l,r,o))
                            
            return ans
        
        return evaluate(expression)

class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:

        def op(l, r, o):
            l, r = int(l), int(r)
            if o == "+":
                return l + r
            elif o == "-":
                return l - r
            else:
                return l * r

        def evaluate(exp, memo={}):
            if "+" not in exp and "-" not in exp and "*" not in exp:
                return [int(exp)]

            if exp in memo:
                return memo[exp]

            ans = []
            for i in range(len(exp)):
                o = exp[i]
                if o in "+-*":
                    left = evaluate(exp[:i])
                    right = evaluate(exp[i+1:])
                    for l in left:
                        for r in right:
                            ans.append(op(l,r,o))

            memo[exp] = ans
            return ans

        return evaluate(expression, {})

