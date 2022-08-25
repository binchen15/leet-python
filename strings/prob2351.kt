class Solution {
    fun repeatedCharacter(s: String): Char {
    
        val hset = mutableSetOf<Char>()
        
        for (c in s) {
            if (c in hset) {
                return c
            } else {
                hset.add(c)
            }
        }
        
        throw Exception("should not happen")
        
    }
}
