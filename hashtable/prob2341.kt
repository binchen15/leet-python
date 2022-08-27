// 2341 Maximum Number of Pairs in Array
//
class Solution {
    fun numberOfPairs(nums: IntArray): IntArray {
        
        val cnts = mutableMapOf<Int, Int>()
        for (v in nums) {
            cnts.put(v, cnts.getOrDefault(v, 0)+1)
        }
        
        val ans = IntArray(2)
        for (v in cnts.values ) {
            ans[0] += v / 2
            ans[1] += v % 2
        }
        
        return ans
        
    }
}
