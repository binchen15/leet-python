// 2357 Make Array Zero by Subtracting Equal Amounts 
class Solution {
    fun minimumOperations(nums: IntArray): Int {
        
        val hm = mutableMapOf<Int, Int>()
        for (v in nums) {
            hm[v] = hm.getOrDefault(v, 0) + 1
        }
        
        //println(hm)
        return hm.filter {e -> e.key > 0} .size
        
    }
}
