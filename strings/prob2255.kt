class Solution {
    fun countPrefixes(words: Array<String>, s: String): Int {
        
        return words.count { it-> s.startsWith(it) }
        
    }
}
