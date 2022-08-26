class Solution {
    fun canBeTypedWords(text: String, brokenLetters: String): Int {
        
        var cnts = 0 
        val s = brokenLetters.toSet()
        
        var words = text.split(" ")
        for (word in words) {
            var flag = true
            for (c in word.toSet()) {
                if (c in s) {
                    flag = false
                    break
                }
            }
            if (flag) cnts++
        }
        
        return cnts
               
    }
}
