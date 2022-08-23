class Solution {
    fun subtractProductAndSum(n: Int): Int {
        
        var digit: Int
        var m = n
        var prod = 1 
        var tot = 0
        
        while (m > 0) {
            digit = m % 10
            prod *= digit
            tot += digit
            m = m / 10
        }

        return prod - tot
        
    }
}
