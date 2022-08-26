class Solution {
    fun checkString(s: String): Boolean {
        
        val a = s.lastIndexOf('a')
        val b = s.indexOf('b')
        if ( a == -1 || b == -1) {
            return true
        }
        
        return a < b
        
    }
}
