class Solution {
    fun countOperations(num1: Int, num2: Int): Int {
        
        var counts = 0
        var n1 = num1
        var n2 = num2
        while (n1 > 0 && n2 > 0) {
            if (n1 >= n2) {
                n1 -= n2
            } else {
                n2 -= n1
            }            
            counts++
        }
        
        return counts
        
    }
}

// 67%
class Solution {
    fun countOperations(num1: Int, num2: Int): Int {

        var counts = 0
        var n1 = num1
        var n2 = num2
        while (n1 > 0 && n2 > 0) {
            if (n1 >= n2) {
                counts += n1/n2
                n1 = n1 % n2
            } else {
                counts += n2/n1
                n2 = n2 % n1
            }

        }

        return counts

    }
}
