// 1342 Number of Steps to Reduce a Number to Zero 
//
// class Solution {
    fun numberOfSteps(num: Int): Int {

        var steps = 0
        var tmp = num
        while (tmp > 0) {
            steps++
            tmp = if (tmp % 2 == 0) tmp/2 else tmp-1
        }

        return steps
    }
}
