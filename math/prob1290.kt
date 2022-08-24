// Convert Binary Number in a Linked List to Integer
/**
 * Example:
 * var li = ListNode(5)
 * var v = li.`val`
 * Definition for singly-linked list.
 * class ListNode(var `val`: Int) {
 *     var next: ListNode? = null
 * }
 */
class Solution {
    fun getDecimalValue(head: ListNode?): Int {

        var ans = 0
        var cur = head
        while (cur != null) {
            ans = ans * 2 + cur.`val`
            cur = cur.next
        }

        return ans

    }
}
