func generateParenthesis(n int) []string {
    
    ans := []string{}
    
    walk("", n, 0, 0, &ans)
    
    return ans
    
}

func walk(s string, n int, left int, right int, ans *[]string) {
    if left == n && right == n {
        *ans = append(*ans, s)
    }
    
    if left < n {
        walk(s + "(", n, left+1, right, ans)
    }
    
    if right < left {
        walk(s + ")", n, left, right+1, ans)
    }
    
}
