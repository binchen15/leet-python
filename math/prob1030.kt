import kotlin.math.abs

class Solution {
    fun allCellsDistOrder(rows: Int, cols: Int, rCenter: Int, cCenter: Int): Array<IntArray> {
           
        val ans = Array<IntArray>(rows*cols, {it -> intArrayOf( it / cols, it % cols) })
        
        return ans.sortedBy {it -> abs(it[0]-rCenter) + abs(it[1]-cCenter) }.toTypedArray()
        
    }
}

import kotlin.math.abs

class Solution {
    fun allCellsDistOrder(rows: Int, cols: Int, rCenter: Int, cCenter: Int): Array<IntArray> {

        val ans = Array<IntArray>(rows*cols, {it -> intArrayOf( it / cols, it % cols) })
        ans.sortWith( compareBy {it -> abs(it[0]-rCenter) + abs(it[1]-cCenter) } )
        return ans
    }
}
