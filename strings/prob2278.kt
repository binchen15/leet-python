class Solution {
    fun percentageLetter(s: String, letter: Char): Int {
        var n = s.length
        var cnt = s.count { it -> it == letter}
        return cnt * 100/ n
    }
}
