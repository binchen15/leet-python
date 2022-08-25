class Solution {
    fun reverseString(s: CharArray): Unit {
        
        val n = s.size
        var l = 0
        var r = n-1
        while (l < r) {
            var tmp = s[l]
            s[l] = s[r]
            s[r] = tmp
            l++
            r--
        } 
        
        
    }
}
