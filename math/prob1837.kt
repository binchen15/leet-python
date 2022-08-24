class Solution {
    
    fun sumBase(n: Int, k: Int): Int {
     
        var m = n
        var ans = 0
        while (m > 0) {
            var r = m % k
            ans += r
            m /= k 
        }
        return ans
    }
}
