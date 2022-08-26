// 1365 How many numbers are smaller than the current number

class Solution {
    fun smallerNumbersThanCurrent(nums: IntArray): IntArray {

        val n = nums.size
        val ans = IntArray(n)

        val hm = mutableMapOf<Int, MutableSet<Int>>()

        for (i in 0 until n) {
            var v = nums[i]
            if (v in hm) {
                hm[v]?.add(i)
            } else {
                hm[v] = mutableSetOf<Int>(i)
            }
        }

        var pairs = hm.toList().sortedBy {(first, second) -> first}

        var psum = 0
        val m = pairs.size

        for (i in 1 until m) {
            psum += pairs[i-1].second.size
            for (j in pairs[i].second) {
                ans[j] = psum
            }
        }

        return ans


    }
}
