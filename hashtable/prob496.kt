class Solution {
    fun nextGreaterElement(nums1: IntArray, nums2: IntArray): IntArray {
        
        val n1 = nums1.size
        val n2 = nums2.size
        var m = mutableMapOf<Int, Int>()
        for (i in 0 until n2) {
            m[nums2[i]] = i
        }
        
        val ans = IntArray(n1) {i-> -1}
        for (i in 0 until n1) {
            var j = m[nums1[i]]!!
           
            for (k in (j+1) until n2) {
                if (nums2[k] > nums1[i]) {
                    
                    ans[i] = nums2[k]
                    break
                }
            }
            
        }
        
        return ans       
    }
}
