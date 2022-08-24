// count of matches in tournament
class Solution {
    fun numberOfMatches(n: Int): Int {

        var tmp = n
        var ans = 0

        while (tmp > 1) {
            if (tmp % 2 == 0) {
                tmp /= 2
                ans += tmp
            } else {
                ans += (tmp-1) / 2
                tmp = (tmp+1)/2
            }
        }

        return ans

    }
}
