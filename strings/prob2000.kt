class Solution {
    fun reversePrefix(word: String, ch: Char): String {
        
        var i = word.indexOf(ch)
        if (i == -1) {
            return word
        }
        
        return word.substring(0..i).reversed() + word.substring((i+1) until word.length)
        
    }
}
