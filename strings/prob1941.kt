class Solution {
    fun areOccurrencesEqual(s: String): Boolean {
        
        val a = IntArray(26)
        for (c in s) {
            a[c-'a']++
        }
        // println(a.toSet())
        return a.filter({it -> it > 0}).toSet().size == 1
        
    }
}
