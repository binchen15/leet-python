// 1266. Minimum Time Visiting All Points
import kotlin.math.abs

class Solution {
    fun minTimeToVisitAllPoints(points: Array<IntArray>): Int {

        val n = points.size
        var secs = 0

        for (i in 1 until n) {
            var dx = abs(points[i][0] - points[i-1][0])
            var dy = abs(points[i][1] - points[i-1][1])
            secs += if (dx >= dy) dx else dy
        }

        return secs


    }
}
