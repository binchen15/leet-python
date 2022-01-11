func isValid(s string) bool {
    
    n := len(s)
    if n % 2 != 0 {
        return false
    }
    
    if n == 0 {
        return true
    }
    
    stack := []rune{}
    
    for _, char := range s {
        if char == '(' || char == '[' || char == '{' {
            stack = append(stack, char)
        } else {
            if len(stack) == 0 {
                return false
            }
            dual := stack[len(stack)-1]
            stack = stack[:len(stack)-1]
            if char ==')' && dual != '(' || char ==']' && dual != '[' || char =='}' && dual != '{' {
                return false
            }
        }
    }
    
    return len(stack) == 0
    
    
}

// use hashmap
func isValid(s string) bool {

    n := len(s)
    if n % 2 != 0 {
        return false
    }

    if n == 0 {
        return true
    }

    stack := []rune{}

    m := map[rune]rune {
        '(': ')',
        '[': ']',
        '{': '}',
    }

    for _, char := range s {
        _, ok := m[char]
        if ok {
            stack = append(stack, char)
        } else {
            if len(stack) == 0 {
                return false
            }
            dual := stack[len(stack)-1]
            stack = stack[:len(stack)-1]
            if m[dual] != char  {
                return false
            }
        }
    }

    return len(stack) == 0

}
