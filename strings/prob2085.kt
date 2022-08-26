class Solution {
    fun countWords(words1: Array<String>, words2: Array<String>): Int {
        
        val s1 = mutableMapOf<String, Int>()
        var s2 = mutableMapOf<String, Int>()
        
        for (word in words1) {
            s1.put(word, s1.getOrDefault(word, 0) + 1)
        }
        
        for (word in words2) {
            s2.put(word, s2.getOrDefault(word, 0) + 1)
        }
        
        var ans = 0
        
        for (word in s1.keys) {
            //println(word.javaClass)
            if (s1.getOrDefault(word, 0) == 1 &&  s2.getOrDefault(word, 0) == 1 ) {
                ans++
            }
        }
        
        return ans
    }
}
