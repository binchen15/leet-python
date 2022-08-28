/* 242 valid anagram*/
class Solution {
    fun isAnagram(s: String, t: String): Boolean {

        val n = s.length
        var m = t.length
        if (m != n) return false

        val helper = fun(s: String): MutableMap<Char, Int> {

            val m = mutableMapOf<Char, Int>()
            for (c in s) {
                m[c] = m.getOrDefault(c, 0)+1
            }
            return m
        }
        val m1 = helper(s)
        var m2 = helper(t)
        return m1 == m2

    }
}
