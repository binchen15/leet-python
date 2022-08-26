// 2309 Greatest English Letter in Upper/Lower case
//
class Solution {
    
    fun greatestLetter(s: String): String {
     
        val hset = s.toSet()
        for (i in 0..25) {
            val c = 'Z' - i
            if (c in hset && (c + ('a' - 'A')) in hset) {
                return c.toString()
            }
        }
        
        return ""
        
    }
}
