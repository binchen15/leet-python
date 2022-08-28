/* 2068 Check Two strings almost equivalent */

class Solution {
    fun checkAlmostEquivalent(word1: String, word2: String): Boolean {

        val helper = fun(word: String): MutableMap<Char, Int> {
            val m = mutableMapOf<Char, Int>()
            for (c in word) {
                m[c] = m.getOrDefault(c, 0) + 1
            }

            return m
        }

        val m1 = helper(word1)
        var m2 = helper(word2)

        for ( (k, v) in m1) {
            if (Math.abs( m2.getOrDefault(k, 0) - v ) > 3) {
                return false
            }

            m2.remove(k)

        }

        for ( (k, v) in m2) {
            if (Math.abs( m1.getOrDefault(k, 0) - v ) > 3) {
                return false
            }
        }

        return true

    }
}
