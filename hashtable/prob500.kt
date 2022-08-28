# 500 Keyboard row

class Solution {
    fun findWords(words: Array<String>): Array<String> {

        val s1 = "qwertyuiop".toSet()
        val s2 = "asdfghjkl".toSet()
        val s3 = "zxcvbnm".toSet()

        return words.filter( fun(it: String): Boolean {
            var t = it.toLowerCase().toSet()
            return s1.containsAll(t) || s2.containsAll(t) || s3.containsAll(t)
        }) .toTypedArray()

    }

}
