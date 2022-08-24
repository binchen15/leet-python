class Solution {
    fun restoreString(s: String, indices: IntArray): String {
        
        val n = s.length
        val tmp = CharArray(n)
        for ( (i, j) in indices.withIndex() ) {
            tmp[j] = s[i]
        }
        return String(tmp)
        
    }
}
