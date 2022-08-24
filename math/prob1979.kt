class Solution {
    fun findGCD(nums: IntArray): Int {
        val lb: Int = nums.min()!!
        var ub: Int = nums.max()!!
        
        return helper(ub, lb)
    }
    
    fun helper(a: Int, b: Int): Int {
        if (a == b) {
            return a
        } else if (a > b) {
            return helper(a-b, b)
        } else {
            return helper(b-a, a)
        }
    }
}
