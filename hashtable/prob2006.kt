// 2006 Count Number of Pairs With Absolute Difference K 

class Solution {

    fun countKDifference(nums: IntArray, k: Int): Int {

        val hm = mutableMapOf<Int, Int>()
        for (v in nums) {
            hm.put(v, hm.getOrDefault(v, 0) + 1)
        }

        var ans = 0
        for (v in hm.keys) {
            ans += hm.getOrDefault(v, 0) * hm.getOrDefault(v+k, 0)
        }

        return ans

    }
}
