class Solution {
    fun findFinalValue(nums: IntArray, original: Int): Int {
        
        val hset = nums.toSet()
        var ans = original
        while (ans in hset) {
            ans *= 2
        }
        
        return ans
        
    }
}
