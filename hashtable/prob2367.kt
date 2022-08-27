// 2367 Number of Arithmetic triplets

class Solution {
    fun arithmeticTriplets(nums: IntArray, diff: Int): Int {

        val hset = nums.toSet()
        return nums.count {it -> (it-diff) in hset && (it+diff) in hset }
    }
}
