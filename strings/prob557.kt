class Solution {
    fun reverseWords(s: String): String {
        return s.split(" ").map {word -> word.reversed() } .joinToString(" ")
    }
}
