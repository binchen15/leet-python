class Solution {
    fun isSumEqual(firstWord: String, secondWord: String, targetWord: String): Boolean {
        return helper(firstWord) + helper(secondWord) == helper(targetWord)
    }
    
    fun helper(word: String): Int {
        return word.map { c -> c - 'a'}.joinToString().toInt()
    }
}
