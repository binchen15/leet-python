// 1021 Remove Outermost parentheses
//
class Solution {
    fun removeOuterParentheses(s: String): String {
        val n = s.length
        if (n == 2) return ""
        
        var l = 0
        var i = 0
        while (i<n) {
            if (s[i] == '(') {
                l++
            } else {
                l--
                if (l == 0) {
                    return s.substring(1 until i) + removeOuterParentheses(s.substring((i+1) until n))
                }
            }
            i++
        }
        
        return ""
    }
}
