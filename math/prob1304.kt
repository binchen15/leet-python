class Solution {
    fun sumZero(n: Int): IntArray {
        
        val ans = IntArray(n)
        
        if (n % 2 == 0) {
            for (i in 0 until n/2) {
                ans[2*i] = i+1
                ans[2*i+1] = -i-1
            }
        } else {
            for (i in 0 until n/2) {
                ans[2*i+1] = i+1
                ans[2*i+1+1] = -i-1
            }
        }
        return ans
        
    }
}
