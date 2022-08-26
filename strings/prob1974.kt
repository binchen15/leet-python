// 1974 Minimum time to type

class Solution {
    fun minTimeToType(word: String): Int {

        val n = word.length
        var ptr = 0 // position of the pointer
        var ans = 0
        for (c in word) {
            var tmp = c - 'a'
            var d = Math.min( Math.abs(tmp-ptr), 26-Math.abs(tmp-ptr))
            ans += d + 1
            ptr = tmp
        }

        return ans
    }
}
