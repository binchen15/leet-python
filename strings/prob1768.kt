// 1768 Merge Strings Alternatively

class Solution {
    fun mergeAlternately(word1: String, word2: String): String {

        val sb = StringBuilder()
        val n1 = word1.length
        val n2 = word2.length
        var i1 = 0
        var i2 = 0
        while (i1 < n1 && i2 < n2) {
            sb.append(word1[i1++])
            sb.append(word2[i2++])
        }
        if (i1 < n1) {
            sb.append(word1.substring(i1 until n1))
        }
        if (i2 < n2) {
            sb.append(word2.substring(i2 until n2))
        }
        return sb.toString()
    }
}
