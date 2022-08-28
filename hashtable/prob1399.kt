/* 1399 Count Largest Group*/

class Solution {
    fun countLargestGroup(n: Int): Int {

        val helper = fun(i: Int): Int {
            var s = 0
            var t = i
            while (t > 0) {
                s += t % 10
                t /= 10
            }
            return s
        }

        var counter = mutableMapOf<Int, Int>()
        for (i in 1..n) {
            val v = helper(i)
            counter[v] = counter.getOrDefault(v, 0) + 1
        }

        val mux = counter.values.max()
        return counter.filter{it-> it.value == mux}.size

    }
}
