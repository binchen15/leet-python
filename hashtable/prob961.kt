class Solution {
    fun repeatedNTimes(nums: IntArray): Int {
        
        var hm = mutableSetOf<Int>()
        for (v in nums) {
            if (v in hm) {
                return v
            } else {
                hm.add(v)
            }
        }
        
        throw Exception("Oops!")
        
    }
}
