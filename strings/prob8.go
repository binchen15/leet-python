import "math"

func myAtoi(s string) int {
    
    n := len(s)
    if n == 0 {
        return 0
    }
    
    max_int := math.MaxInt32
    min_int := math.MinInt32
    tot := 0
    sign := 1
    
    i := 0
    for i < n && s[i] == byte(' ') {
        i++
    }
    if i == n {
        return 0
    }
    
    if s[i] == byte('+') || s[i] == byte('-') {
        if s[i] == byte('-') {
            sign = -1
        }
        i += 1
    }
    
    for i < n {
        digit := int(s[i] - byte('0'))
        if digit < 0 || digit > 9 {
            break
        }
        if tot > max_int / 10 || (tot == max_int / 10 && digit > max_int % 10) {
            if sign == 1 {
                return max_int
            } else {
                return min_int
            }
        } else {
            tot = tot * 10 + digit
        }
        i++
    }
    
    if sign == 1 {
        return tot
    } else {
        return -tot
    }
    
}
