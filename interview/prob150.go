import (
    "strings"
    "strconv"
)

func evalRPN(tokens []string) int {
    
    stack := []int{}
    
    for _, t := range tokens {
        if strings.Contains("+-*/", t) {
            sz := len(stack)
            a, b := stack[sz-2], stack[sz-1]
            c := eval(a, b, t)
            stack = append(stack[:sz-2], c)
        } else {
            v, _ := strconv.Atoi(t)
            stack = append(stack, v)
        }
    }
    
    return stack[0]
    
}

func eval(a int, b int, op string) int {
    if op == "+" {
        return a + b
    } else if op == "-" {
        return a - b
    } else if op == "*" {
        return a * b
    } else {
        return a / b
    }
}
