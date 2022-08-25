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
