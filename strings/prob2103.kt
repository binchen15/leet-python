// Rings and Rods 2103

class Solution {
    fun countPoints(rings: String): Int {

        val n = rings.length
        val m = mutableMapOf<Char, MutableSet<Char>>()

        for (i in 0 until n step 2) {
            var color = rings[i]
            var rod = rings[i+1]
            if (m.containsKey(rod)) {
                m[rod]?.add(color)
            } else {
                m.put(rod, mutableSetOf(color))
            }
        }

        return m.values.map {it.size}.filter {it == 3}.size

    }
}
