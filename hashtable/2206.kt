// Divide Array Into Equal Pairs
class Solution {
    fun divideArray(nums: IntArray): Boolean {
        
        val counter = mutableMapOf<Int, Int>()
        for (v in nums) {
            counter[v] = counter.getOrDefault(v, 0)+1
        }
        
        for (value in counter.values) {
            if (value % 2 != 0) {
                return false
            }
        }
        return true
    }
}
