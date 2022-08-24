class Solution {

    fun subsetXORSum(nums: IntArray): Int {
        val n = nums.size
        val ans = IntArray(1)
        val l = mutableListOf<Int>()
        walk(l, nums, ans)
        return ans[0]
    }

    fun walk(arr: MutableList<Int>, nums: IntArray, ans: IntArray) {
        val m = arr.size
        val n = nums.size
        if (m == n) {
            ans[0] += helper(arr)
        } else {
            arr.add(0)
            walk(arr, nums, ans)
            // arr.removeLast()
            arr.removeAt(arr.size-1)
            arr.add(nums[m])
            walk(arr, nums, ans)
            arr.removeAt(arr.size-1)
        }
    }

    fun helper(arr: MutableList<Int>): Int {
        val n = arr.size
        var ans = arr.reduce {acc, it -> acc xor it}
        return ans
    }
}
