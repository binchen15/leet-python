class Solution {
    fun sortSentence(s: String): String {
        
        var parts = s.split(" ")
        var n = parts.size
        var tmp = Array<String>(n, {it-> ""})
        for (word in parts) {
            tmp[word.last()-'1'] = word.substring(0..(word.length-2))
        }
        
        return tmp.joinToString(" ")
        
    }
}
