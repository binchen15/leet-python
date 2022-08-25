class Solution {
    fun firstPalindrome(words: Array<String>): String {
        for (word in words) {
            if (helper(word)) {
                return word
            }
        }
        return ""
    }
    
    fun helper(s: String): Boolean {
        if (s == "") {
            return true
        }
        var l = 0
        var r = s.length - 1
        while (l < r) {
            if (s[l] != s[r]) {
                return false
            }
            l++
            r--
        }
        return true
    }
    
}
