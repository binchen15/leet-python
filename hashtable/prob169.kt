/* 169 Majority Element */
 
class Solution {
    fun majorityElement(nums: IntArray): Int {
        
        var m = mutableMapOf<Int, Int>()
        for (v in nums) {
            m[v] = m.getOrDefault(v, 0) + 1
        }
        
        var bar = nums.size/2
        for ((k, v) in m) {
            if (v > bar) {
                return k
            }
        }
        
        return -1
        
    }
}
