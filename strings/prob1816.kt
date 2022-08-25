// 1816

class Solution {
    fun truncateSentence(s: String, k: Int): String {

        var tmp = s.split(" ")
        var ans = StringBuilder()
        for (i in 0 until k) {
            ans.append(tmp[i])
            if (i < k-1) {
                ans.append(" ")
            }
        }

        return ans.toString()

    }
}

class Solution {
    fun truncateSentence(s: String, k: Int): String {

        val n = s.length
        var i = 0
        var cnt = 0
        while (i < n) {
            if (s[i] == ' ') {
                cnt++
                if (cnt == k) {
                    return s.substring(0..(i-1))
                }
            }
            i++
        }
        return s

    }
}
