// 1588 Sum of All Odd Length Subarrays 
class Solution {
    fun sumOddLengthSubarrays(arr: IntArray): Int {
        val n = arr.size
        var ans = 0
        val psum = IntArray(n+1)
        psum[0] = 0 // arr[0]
        for (i in 1 .. n) {
            psum[i] = psum[i-1] + arr[i-1]
        }
        
        for (i in 0 until n) {
            for (j in i until n step 2) {
                // arr[i:j]
                val tmp = psum[j+1] - psum[i]
                ans += tmp
            }
        }
        
        return ans
        
    }
}
