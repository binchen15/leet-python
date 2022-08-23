// brutal force. Number of good pairs`
class Solution {
    fun numIdenticalPairs(nums: IntArray): Int {
        var ans = 0
        for (i in 0 until nums.size) {
            for (j in i+1 until nums.size) {
                if (nums[i] == nums[j]) {
                    ans++
                }
            }
        }
        return ans
    }
}
