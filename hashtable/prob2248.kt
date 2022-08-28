# intersection of multiple arrays

class Solution {
    fun intersection(nums: Array<IntArray>): List<Int> {

        return nums.map{ it -> it.toSet()} .reduce { acc, it -> acc.intersect(it) } .toList().sorted()

    }
}
