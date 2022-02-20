class Solution:
    def complexNumberMultiply(self, num1: str, num2: str) -> str:
        
        def parse(num):
            l = num.split("+")
            real = int(l[0])
            sec = l[1]
            imaginary = int(sec[:len(sec)-1])
        
            return (real, imaginary) 
        
        def form(real, imaginary):
            
            return f"{real}+{imaginary}i"
                
        def prod(num1, num2):
            
            x1, y1 = num1
            x2, y2 = num2
            return (x1*x2 - y1*y2, x1*y2+x2*y1)
        
        
        z1 = parse(num1)
        z2 = parse(num2)
        
        z3 = form(*prod(z1, z2))
        
        return z3
