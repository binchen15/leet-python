// brutal force. Number of good pairs`
class Solution {
    fun numIdenticalPairs(nums: IntArray): Int {
        var ans = 0
        for (i in 0 until nums.size) {
            for (j in i+1 until nums.size) {
                if (nums[i] == nums[j]) {
                    ans++
                }
            }
        }
        return ans
    }
}

// map based solution
class Solution {
    fun numIdenticalPairs(nums: IntArray): Int {
        var ans = 0
        val map: MutableMap<Int, Int> = mutableMapOf()
        for (v in nums) {
            map.put(v, map.getOrDefault(v, 0) + 1 )
        }
        for ((k, v) in map){
            if (v > 1) {
                ans += v*(v-1)/2
            }
        }
        return ans
    }
}
