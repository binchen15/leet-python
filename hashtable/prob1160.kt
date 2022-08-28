class Solution {
    fun countCharacters(words: Array<String>, chars: String): Int {
        
        var m = mutableMapOf<Char, Int>()
        for (c in chars) {
            m[c] = m.getOrDefault(c, 0) + 1
        }
    
        val f = fun(word: String, m: MutableMap<Char,Int>): Boolean {
            var m1 = mutableMapOf<Char, Int>()
            for (c in word) {
                m1[c] = m1.getOrDefault(c, 0) + 1
            }
            for ( (k, v) in m1 ) {
                if (v > m.getOrDefault(k, 0)) {
                    return false
                }
            }
            return true
        }
        
        return words.filter({it -> f(it, m)}).fold(0) { acc, it-> acc + it.length}
        
    }

}
