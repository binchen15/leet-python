// 1221 Recursion
//
class Solution {
    fun balancedStringSplit(s: String): Int {
        
        val n = s.length
        if (n == 0) {
            return 0
        }
        
        var cl = 0 
        var cr = 0
        if (s[0] == 'R') {
            cr++
        } else {
            cl++
        }
        var i = 0
        while (cr != cl && i < n-1) {
            i++
            if (s[i] == 'R') {
                cr++
            } else {
                cl++
            }
        }
        
        return 1 + balancedStringSplit(s.substring((i+1)..(n-1)))
        
    }
}
