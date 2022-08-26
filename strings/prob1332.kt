// 1332 Remove Palin Subsequence
class Solution {
    fun removePalindromeSub(s: String): Int {
        
        val n = s.length
        if (n <= 1) {
            return n
        }
        
        if (helper(s)) {
            return 1
        } else {
            return 2
        }
    
    }
    
    fun helper(s: String): Boolean {
        val n = s.length
        var l = 0
        var r = n-1
        while (l < r) {
            if (s[l] != s[r]) {
                return false
            }
            l++
            r--
        }
        return true
    } 
}
