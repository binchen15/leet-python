// 1742. Maximum Number of Balls in a Box
class Solution {
    fun countBalls(lowLimit: Int, highLimit: Int): Int {

        var counter = mutableMapOf<Int, Int>()
        var tmp: Int
        for (n in lowLimit..highLimit) {
            tmp = helper(n)
            counter.put(tmp, counter.getOrDefault(tmp, 0) + 1)
        }

        return counter.values.max()!!


    }

    fun helper(n: Int): Int {
        var ans = 0
        var m = n
        while (m > 0) {
            ans += m % 10
            m /= 10
        }
        return ans
    }
}
