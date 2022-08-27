// 2032 Two out of three

class Solution {
    fun twoOutOfThree(nums1: IntArray, nums2: IntArray, nums3: IntArray): List<Int> {

        val counter = mutableMapOf<Int, Int>()
        for (v in nums1.toSet()) {
            counter[v] = counter.getOrDefault(v, 0) + 1
        }
        for (v in nums2.toSet()) {
            counter[v] = counter.getOrDefault(v, 0) + 1
        }
        for (v in nums3.toSet()) {
            counter[v] = counter.getOrDefault(v, 0) + 1
        }

        return counter.filter {(_, value) -> value >= 2}.map{ (key, _) -> key}

    }
}
