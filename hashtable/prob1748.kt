class Solution {
    fun sumOfUnique(nums: IntArray): Int {
        val hm = mutableMapOf<Int, Int>()
        for (v in nums) {
            hm.put(v, hm.getOrDefault(v, 0)+1)
        }
        
        return hm.toList().filter { (k, v) -> v == 1}.map{(k, v) -> k}.sum()
        
    }
}
