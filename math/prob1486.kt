// 1486 XOR operation in an Array
class Solution {
    fun xorOperation(n: Int, start: Int): Int {

        var ans = start
        var tmp = start
        for (i in 1..(n-1)) {
            tmp += 2
            ans = ans xor tmp
        }
        return ans
    }
}
