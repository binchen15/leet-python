// 1876. Substrings of Size Three with Distinct Characters
class Solution {
    fun countGoodSubstrings(s: String): Int {
        val n = s.length
        var ans = 0
        for (i in 0 until n-2) {
            if (s[i] != s[i+1] && s[i+1] != s[i+2] && s[i] != s[i+2]) ans++
        }
        
        return ans
    }
}
