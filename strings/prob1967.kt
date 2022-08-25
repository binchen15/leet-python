class Solution {
    fun numOfStrings(patterns: Array<String>, word: String): Int {
        
        return patterns.filter {it in word}.size
        
    }
}
